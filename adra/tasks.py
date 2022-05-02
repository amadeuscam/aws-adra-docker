from datetime import datetime
import sendgrid
from django.conf import settings
from celery.schedules import crontab
from celery.utils.log import get_task_logger
from adra_project.celery import app
from adra.api_consume.get_api_data import get_caducidades

logger = get_task_logger(__name__)


def send_email_sendgrid(name: str, email_lst: list) -> int:
    message = sendgrid.Mail(
        from_email="admin@adra.es",
        subject=f"El {name} va a caducar pronto",
        to_emails=email_lst,
    )
    message.dynamic_template_data = {
        "alimento": f"{name}",
        "Sender_Name": "Adra Torrejon de ardoz",
        "Sender_Address": "calle primavera 15",
        "Sender_City": "Torrejon de ardoz",
        "Sender_State": "Madrid",
        "Sender_Zip": "28850",
    }
    message.template_id = str(settings.SENDGRID_ALIMENTOS_TEMPLATE_ID)

    try:
        sg = sendgrid.SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return response.status_code
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
    except Exception as e:
        print(e.message)


def check_caducidad(fecha):
    date_format = "%Y-%m-%d"
    a = datetime.strptime(str(datetime.now().date()), date_format)
    b = datetime.strptime(str(fecha), date_format)
    delta_aceite = b - a
    return delta_aceite.days


@app.on_after_finalize.connect
def setup_periodic_tasks(**kwargs):

    # Executes every day  at 8 am
    app.add_periodic_task(
        crontab(minute=0, hour="8,21"),
        caducidad_alimentos,
        name="comprobar las caducidades de los alimentos",
    )


@app.task(bind=True)
def caducidad_alimentos(self) -> str:
    ds = get_caducidades(["almacen", "users"])
    users_data = ds["users"]
    data_aliemntos = ds["almacen"][0]

    list_email = [e["email"] for e in users_data]
    # list_email_test = ["amadeuscam@yahoo.es"]

    for number in range(1, 14):
        if (
            check_caducidad(data_aliemntos[f"alimento_{number}_caducidad"])
            == 37
        ):
            send_email_sendgrid(
                data_aliemntos[f"alimento_{number}_name"], list_email
            )
            return "tarea executada correctamente"
