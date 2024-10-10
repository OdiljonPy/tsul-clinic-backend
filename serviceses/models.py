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

oylar = {
    1: "yanvar",
    2: "fevral",
    3: "mart",
    4: "aprel",
    5: "may",
    6: "iyun",
    7: "iyul",
    8: "avgust",
    9: "sentyabr",
    10: "oktyabr",
    11: "noyabr",
    12: "dekabr"
}


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
    order_number = models.BigIntegerField(blank=True, null=True, verbose_name="Номер заказа")
    document_category = models.ForeignKey(DocumentCategory, on_delete=models.SET_NULL, null=True,
                                          verbose_name="Категория документа")
    price = models.PositiveIntegerField(default=0, blank=True)
    document_type = models.ForeignKey(DocumentType, on_delete=models.SET_NULL, null=True, verbose_name="Тип документа")
    customer_full_name = models.CharField(max_length=250, verbose_name="Полное имя клиента")
    customer_phone = models.CharField(max_length=20, verbose_name="Номер телефона клиента")
    customer_email = models.EmailField(null=True, blank=True, verbose_name="Электронная почьта клиента")
    customer_message = models.TextField(max_length=1000, verbose_name="Сообщение клиента")
    status = models.IntegerField(default=0, choices=DOCUMENT_ORDER_STATUS, verbose_name="Статус")
    file = models.FileField(upload_to='order/document/', null=True, blank=True)

    def __str__(self):
        return self.customer_full_name

    class Meta:
        verbose_name = "Заказ документа"
        verbose_name_plural = "Заказы документов"
        ordering = ('created_at',)

    def save(self, *args, **kwargs):
        if self.order_number is None:
            last_order = DocumentOrder.objects.all().order_by('id').last()
            if last_order:
                self.order_number = 100000000 + last_order.id + 1
            else:
                self.order_number = 100000000
        super().save(*args, **kwargs)


@receiver(pre_save, sender=DocumentOrder)
def track_old_instance(sender, instance, **kwargs):
    if instance.pk:
        # Store the old instance's status in the instance itself
        old_instance = sender.objects.get(pk=instance.pk)
        instance._old_status = old_instance.status


@receiver(pre_save, sender=DocumentOrder)
def track_old_instance(sender, instance, **kwargs):
    if instance.pk:
        instance._old_status = sender.objects.filter(pk=instance.pk).values('status').first()['status']


@receiver(post_save, sender=DocumentOrder)
def create_document_notification(sender, instance, created, **kwargs):
    if created:
        message_create(
            get_message(MessageEnumCode.CREATE),
            item1=instance.order_number,
            recipient=instance.customer_phone,
            user_id=instance.id
        )
    elif hasattr(instance, '_old_status') and instance._old_status != instance.status:
        status_messages = {
            1: get_message(MessageEnumCode.PAYMENT_RECEIVED),
            2: "ko'rib chiqilmoqta",
            3: "tayyor",
            4: "bekor qilindi"
        }
        status_message = status_messages.get(instance.status)

        if status_message:
            message_create(
                get_message(MessageEnumCode.CHANGE_STATUS_DOCUMENT) if instance.status > 1 else status_message,
                item1=instance.order_number,
                item2=status_message if instance.status > 1 else None,
                recipient=instance.customer_phone,
                user_id=instance.id
            )


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
    order_number = models.BigIntegerField(blank=True, null=True, verbose_name="Номен заказа")
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

    def save(self, *args, **kwargs):
        if self.order_number is None:
            last_order = MeetingOrder.objects.all().order_by('id').last()
            if last_order:
                self.order_number = 500000000 + last_order.id + 1
            else:
                self.order_number = 500000000
        super().save(*args, **kwargs)

    def get_meeting_time_as_text(self):
        if self.meeting_time:
            kun = self.meeting_time.day
            oy = oylar[self.meeting_time.month]
            soat = self.meeting_time.strftime("%H:%M")
            return f"{kun}-{oy} soat {soat}"
        return "Время встречи не задано"


@receiver(pre_save, sender=MeetingOrder)
def track_old_instance(sender, instance, **kwargs):
    # Capture the old instance data before saving the updated instance
    if instance.pk:
        instance._old_instance = sender.objects.filter(pk=instance.pk).values('meeting_time', 'meeting_type',
                                                                              'meeting_status').first()


@receiver(post_save, sender=MeetingOrder)
def create_meeting_notification(sender, instance, created, **kwargs):
    # Handle notifications for newly created or updated MeetingOrders
    if created:
        # Send message for new order creation
        message_create(
            get_message(MessageEnumCode.CREATE),
            item1=instance.order_number,
            recipient=instance.customer_phone,
            user_id=instance.id
        )
    else:
        # Handle updates for meeting_time, meeting_type, and meeting_status
        if hasattr(instance, '_old_instance'):
            old_meeting_time = instance._old_instance['meeting_time']
            old_meeting_type = instance._old_instance['meeting_type']
            old_meeting_status = instance._old_instance['meeting_status']

            # Check for meeting time change and relevant meeting type
            if instance.meeting_status == 1 and old_meeting_time != instance.meeting_time:
                if instance.meeting_type == 1:
                    message_type = MessageEnumCode.VIDEO_MEETING_TIME
                elif instance.meeting_type == 0:
                    message_type = MessageEnumCode.PHONE_MEETING_TIME
                elif instance.meeting_type == 3:
                    message_type = MessageEnumCode.MEETING_TIME
                else:
                    message_type = None

                if message_type:
                    message_create(
                        get_message(message_type),
                        item1=instance.order_number,
                        item2=instance.get_meeting_time_as_text(),
                        recipient=instance.customer_phone,
                        user_id=instance.id
                    )
            # Check for meeting status changes
            if instance.meeting_status == 2:
                # Uchrashuv yakunlandi
                message_create(
                    get_message(MessageEnumCode.CHANGE_STATUS_DOCUMENT),
                    item1=instance.order_number,
                    item2="Uchrashuv yakunlandi",
                    recipient=instance.customer_phone,
                    user_id=instance.id
                )
            elif instance.meeting_status == 3:
                # Uchrashuv bekor qilindi
                message_create(
                    get_message(MessageEnumCode.CHANGE_STATUS_DOCUMENT),
                    item1=instance.order_number,
                    item2="Uchrashuv bekor qilindi",
                    recipient=instance.customer_phone,
                    user_id=instance.id
                )


class Contacts(base_models.BaseModel):
    full_name = models.CharField(max_length=150, verbose_name="Полное имя")
    email = models.EmailField(null=True, blank=True, verbose_name="Электронная почьта")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    type = models.ForeignKey(DocumentCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Тип")
    message = models.TextField(max_length=1000, verbose_name="Сообщение")
    file = models.FileField(upload_to='contacts/document/', null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ('created_at',)


class Complaint(base_models.BaseModel):
    order_document = models.ForeignKey(DocumentOrder, on_delete=models.CASCADE)
    complaint = models.TextField()

    def __str__(self):
        return self.complaint[:20]

    class Meta:
        verbose_name = "Жалоба"
        verbose_name_plural = "Жалобы"
        ordering = ('created_at',)
