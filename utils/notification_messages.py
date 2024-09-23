from enum import Enum
from typing import Any


class MessageEnumCode(Enum):
    CREATE_MEETING = 1
    CREATE_DOCUMENT = 2
    PAYMENT_RECEIVED = 3
    CHANGE_STATUS_DOCUMENT = 4
    VIDEO_MEETING_TIME = 5
    PHONE_MEETING_TIME = 6
    MEETING_TIME = 7


MESSAGES = {
    1: {'message': "{} raqamli so'rovingiz qabul qilindi"},
    2: {'message': "{} raqamli hujjat buyurtmangiz yaratildi.\nTo'lov qilingandan so'ng buyurtma faollashadi"},
    3: {'message': "{} raqamli so'rovingiz uchun to'lov qabul qilindi"},
    4: {'message': "{} raqamli so'rovingiz holati: {} ga o'zgartirildi "},
    5: {'message': "{} raqamli video uchrashuv {} vaqtga belgilandi"},
    6: {'message': "{} raqamli telefon orqali muloqot {} vaqtga belgilandi"},
    7: {'message': "{} raqamli konsultatsiya {} vaqtga belgilandi"}
}


def get_message(enum_code) -> dict[str, Any]:
    return MESSAGES.get(enum_code.value, {'message': None})

