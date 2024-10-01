import time

import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth


def send_notification(message: str) -> None:
    try:
        print(requests.get(settings.TELEGRAM_API_URL + message))
    except Exception as e:
        print(f"Failed while sending request to telegram client: {e}")


def message_create(message: dict[str, str], recipient, user_id, item1: str = "N/A", item2: str = "unknown"):
    message = message.get('message').format(*[item1, item2, settings.BASE_URL])
    send_message(message, recipient=recipient, user_id=user_id)


def send_message(message: str, recipient: str, user_id: int):
    """
    Funksiya xabarlarni yuborish uchun POST so'rovini yuboradi.

    :param message: Yuboriladigan xabar ma'lumotlari
    :param recipient: Xabar yuboriladigan telefon raqam
    :param user_id: Yuboriladigan userning id raqami
    :return: API javobi
    """
    url = f"{settings.SMS_BASE_URL}/send"
    # Takrorlanmas message-id yaratish uchun vaqt asosida o'zgacha ketma-ketlik yaratamiz
    message_id = f"tsul{user_id}{int(time.time())}"
    messages = {
        "messages":
            [
                {
                    "recipient": recipient,
                    "message-id": message_id,

                    "sms": {

                        "originator": "3700",
                        "content": {
                            "text": message
                        }
                    }
                }
            ]
    }

    # sms junatish
    response = requests.post(
        url,
        auth=HTTPBasicAuth(settings.SMS_USERNAME, settings.SMS_PASSWORD),
        json=messages
    )
    print('=' * 50, "SMS", '=' * 50, )
    print('-' * 50, 'json', '-' * 50, )
    print(messages)
    print('-' * 50, 'json', '-' * 50, )
    print(response)
    print('=' * 50, "SMS", '=' * 50, )
    # Javobni qaytarish
    return response
