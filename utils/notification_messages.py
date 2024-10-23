from enum import Enum


class MessageEnumCode(Enum):
    CREATE = 1
    PAYMENT_RECEIVED = 2
    CHANGE_STATUS_DOCUMENT = 3
    VIDEO_MEETING_TIME = 4
    PHONE_MEETING_TIME = 5
    MEETING_TIME = 6


MESSAGES = {
    1: {
        'message': "{} raqamli so'rovingiz muvaffaqiyatli qabul qilindi.\nBatafsil ma'lumot uchun saytga tashrif buyuring: {}"},
    2: {
        'message': "{} raqamli so'rovingiz uchun to'lov muvaffaqiyatli qabul qilindi.\nBatafsil ma'lumot uchun saytga tashrif buyuring: {}"},
    3: {
        'message': "{} raqamli so'rovingiz holati {} ga o'zgartirildi.\nBatafsil ma'lumot uchun saytga tashrif buyuring: {}"},
    4: {
        'message': "{} raqamli video uchrashuv {} vaqtga belgilandi.\nBatafsil ma'lumot uchun saytga tashrif buyuring: {}"},
    5: {
        'message': "{} raqamli telefon orqali muloqot {} vaqtga belgilandi.\nBatafsil ma'lumot uchun saytga tashrif buyuring: {}"},
    6: {
        'message': "{} raqamli konsultatsiya {} vaqtga belgilandi.\nBatafsil ma'lumot uchun saytga tashrif buyuring: {}"}

}


def get_message(enum_code):
    return MESSAGES.get(enum_code.value, {'message': None})


def create_message_telegram(customer_full_name, phone_number, language, type, description, url):
    message = ("Tsul Klinik\n"
               f"Murojatchi F.I.O: {customer_full_name}\n"
               f"Murojatchi telefon raqami: {phone_number}\n"
               f"Murojat haqida: {description}\n"
               f"Murojat tili: {language}\n"
               f"Murojat turi: {type}"
               f"Url: {url}")

    return message
