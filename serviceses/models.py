from shutil import posix

from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from abstract_models import base_models
from utils.notification_messages import get_message, MessageEnumCode
from utils.send_notifications import message_create

DOCUMENT_ORDER_STATUS = (
    (0, 'ОЖИДАЕТСЯ ПЛАТЕЖ'),
    (1, 'ДОКУМЕНТ ПРИНЯТ'),
    (2, 'РАССМАТРИВАЕТЬСЯ'),
    (3, 'ЗАВЕРШЕННЫЙ'),
    (4, 'ОТМЕНЕНО')

)
MEETING_ORDER_TYPES = (
    (0, 'ЗВОНОК'),
    (1, 'ВИДЕО ЗВОНОК'),
    (2, 'ВСТРЕЧА')
)

MEETING_ORDER_STATUS = (
    (0, 'ОЖИДАЕТСЯ ПЛАТЕЖ'),
    (1, 'ПРИНЯТ'),
    (2, 'ЗАВЕРШЕННЫЙ'),
    (3, 'ОТМЕНЕНО')
)


class DocumentCategory(base_models.BaseModel):
    category_name = models.CharField(max_length=150, verbose_name="Название категории")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Категория документа"
        verbose_name_plural = "Категории документов"
        ordering = ('created_at',)


class DocumentType(base_models.BaseModel):
    document_name = models.CharField(max_length=150, verbose_name="Название документа")
    document_category = models.ForeignKey(DocumentCategory, on_delete=models.CASCADE,
                                          verbose_name="Категория документа")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    def __str__(self):
        return self.document_name

    class Meta:
        verbose_name = "Тип документа"
        verbose_name_plural = "Типы документов"
        ordering = ("created_at",)


class DocumentOrder(base_models.BaseModel):
    order_number = models.CharField(max_length=150, blank=True, null=True, verbose_name="Номер заказа")
    document_category = models.ForeignKey(DocumentCategory, on_delete=models.SET_NULL, null=True,
                                          verbose_name="Категория документа")
    price = models.PositiveIntegerField(default=0, blank=True)
    document_type = models.ForeignKey(DocumentType, on_delete=models.SET_NULL, null=True, verbose_name="Тип документа")
    customer_full_name = models.CharField(max_length=250, verbose_name="Полное имя клиента")
    customer_phone = models.CharField(max_length=20, verbose_name="Номер телефона клиента")
    customer_email = models.EmailField(null=True, blank=True, verbose_name="Электронная почьта клиента")
    customer_message = models.TextField(max_length=1000, verbose_name="Сообщение клиента")
    status = models.IntegerField(default=0, choices=DOCUMENT_ORDER_STATUS, verbose_name="Статус")

    def __str__(self):
        return self.customer_full_name

    class Meta:
        verbose_name = "Заказ документа"
        verbose_name_plural = "Заказы документов"
        ordering = ('created_at',)


@receiver([post_save], sender=DocumentOrder)
def create_document_notification(sender, instance, **kwargs):
    if kwargs.get('created', False):
        message_create(get_message(MessageEnumCode.CREATE), item1=instance.order_number,
                       recipient=instance.customer_phone, user_id=instance.id)
        return
    old_instance = sender.objects.get(pk=instance.pk)
    if old_instance.status != instance.status and instance.status == 1:
        message_create(get_message(MessageEnumCode.PAYMENT_RECEIVED), item1=instance.order_number,
                       recipient=instance.customer_phone, user_id=instance.id)
        return
    if old_instance.status != instance.status and instance.status != 1:
        message_create(get_message(MessageEnumCode.CHANGE_STATUS_DOCUMENT), item1=instance.order_number,
                       item2=dict(DOCUMENT_ORDER_STATUS).get(instance.status), recipient=instance.customer_phone,
                       user_id=instance.id)
        return


class ReadyDocuments(base_models.BaseModel):
    document_order = models.ForeignKey(DocumentOrder, on_delete=models.CASCADE, verbose_name="Заказ документа")
    document_name = models.CharField(max_length=250, verbose_name="Название документа")
    document = models.FileField(upload_to="documents/%Y/%m/%d", verbose_name="Документ")

    def __str__(self):
        return self.document_name

    class Meta:
        verbose_name = "Готовый документ"
        verbose_name_plural = "Готовые документы"
        ordering = ('created_at',)


class MeetingOrder(base_models.BaseModel):
    order_number = models.CharField(max_length=150, blank=True, null=True, verbose_name="Номен заказа")
    customer_full_name = models.CharField(max_length=150, verbose_name="Полное имя клиента")
    customer_phone = models.CharField(max_length=20, verbose_name="Номер телефона клиента")
    customer_email = models.EmailField(null=True, blank=True, verbose_name="Электронная почьта клиента")
    meeting_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                        verbose_name="Цена встечи")
    meeting_status = models.IntegerField(default=0, choices=MEETING_ORDER_STATUS, verbose_name="Статус встречи")
    meeting_type = models.IntegerField(choices=MEETING_ORDER_TYPES, verbose_name="Тип встречи")
    meeting_time = models.DateTimeField(null=True, blank=True, verbose_name="Время встречи")

    def __str__(self):
        return self.customer_full_name

    class Meta:
        verbose_name = "Заказ встречи"
        verbose_name_plural = "Заказы встречь"
        ordering = ('created_at',)


@receiver([post_save], sender=MeetingOrder)
def create_meeting_notification(sender, instance, **kwargs):
    if kwargs.get('created', False):
        message_create(get_message(MessageEnumCode.CREATE), item1=instance.order_number,
                       recipient=instance.customer_phone, user_id=instance.id)
        return
    old_instance = sender.objects.get(pk=instance.pk)
    if old_instance.meeting_time == instance.meeting_time and instance.meeting_type == 0:
        message_create(get_message(MessageEnumCode.PHONE_MEETING_TIME), item1=instance.order_number,
                       item2=instance.meeting_time, recipient=instance.customer_phone, user_id=instance.id)
        return
    if old_instance.meeting_time == instance.meeting_time and instance.meeting_type == 1:
        message_create(get_message(MessageEnumCode.VIDEO_MEETING_TIME), item1=instance.order_number,
                       item2=instance.meeting_time, recipient=instance.customer_phone, user_id=instance.id)
        return
    if old_instance.meeting_time == instance.meeting_time and instance.meeting_type == 2:
        message_create(get_message(MessageEnumCode.VIDEO_MEETING_TIME), item1=instance.order_number,
                       item2=instance.meeting_time, recipient=instance.customer_phone, user_id=instance.id)
        return


class Contacts(base_models.BaseModel):
    full_name = models.CharField(max_length=150, verbose_name="Полное имя")
    email = models.EmailField(null=True, blank=True, verbose_name="Электронная почьта")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    type = models.ForeignKey(DocumentCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Тип")
    message = models.TextField(max_length=1000, verbose_name="Сообщение")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Контракт"
        verbose_name_plural = "Контракты"
        ordering = ('created_at',)
