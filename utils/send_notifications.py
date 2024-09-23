import requests
from django.conf import settings


def send_notification(message: str) -> None:
    try:
        print(requests.get(settings.TELEGRAM_API_URL + message))
    except Exception as e:
        print(f"Failed while sending request to telegram client: {e}")


def message_create(message: dict[str, str], item1=None, item2=None):
    message = message.get('message').format(*[item1, item2])
    send_notification(message)
