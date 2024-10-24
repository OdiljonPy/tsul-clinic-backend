from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.conf import settings
from abstract_models import base_models
from serviceses.utils import validate_uz_number, validate_rating
from utils.notification_messages import get_message, MessageEnumCode, create_message_telegram
from utils.send_notifications import message_create, send_notification

DOCUMENT_ORDER_STATUS = (
    (0, 'ОЖИДАЕТСЯ'),
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
    (0, 'ОЖИДАЕТСЯ'),
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


class DocumentOrder(base_models.BaseModel):
    order_number = models.BigIntegerField(blank=True, null=True, verbose_name="Номер заказа")
    price = models.PositiveIntegerField(default=0, blank=True, verbose_name="Цена")
    expert = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Эксперт")
    document_type = models.TextField(max_length=255, null=True, verbose_name="Краткое описание проблемы")
    customer_full_name = models.CharField(max_length=250, verbose_name="Полное имя клиента")
    customer_phone = models.CharField(max_length=20, verbose_name="Номер телефона клиента")
    customer_email = models.EmailField(null=True, blank=True, verbose_name="Электронная почьта клиента")
    customer_message = models.TextField(max_length=1000, verbose_name="Сообщение клиента")
    status = models.IntegerField(default=0, choices=DOCUMENT_ORDER_STATUS, verbose_name="Статус")
    file = models.FileField(upload_to='order/document/', null=True, blank=True, verbose_name="Файл")

    def __str__(self):
        return self.customer_full_name

    class Meta:
        verbose_name = "Заказ документа"
        verbose_name_plural = "Заказы документов"
        ordering = ('-created_at',)

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


def default_meeting_end_time():
    return timezone.now() + timezone.timedelta(minutes=30)


class MeetingOrder(base_models.BaseModel):
    order_number = models.BigIntegerField(blank=True, null=True, verbose_name="Номен заказа")
    customer_full_name = models.CharField(max_length=150, verbose_name="Полное имя клиента")
    customer_phone = models.CharField(max_length=20, verbose_name="Номер телефона клиента")
    customer_email = models.EmailField(null=True, blank=True, verbose_name="Электронная почьта клиента")
    meeting_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                        verbose_name="Цена встечи", default=0)
    language = models.CharField(max_length=3, null=True, blank=True, verbose_name='Язык')
    expert = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Эксперт")
    short_description = models.TextField(max_length=255, null=True, blank=True, verbose_name='Краткое описание проблемы')
    meeting_status = models.IntegerField(default=0, choices=MEETING_ORDER_STATUS, verbose_name="Статус встречи")
    meeting_type = models.IntegerField(choices=MEETING_ORDER_TYPES, verbose_name="Тип встречи")
    meeting_time = models.DateTimeField(null=True, blank=True, verbose_name="Время встречи", default=timezone.now())
    meeting_end_time = models.TimeField(null=True, blank=True, verbose_name="Время встречи",
                                        default=default_meeting_end_time)

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


class MeetingLink(base_models.BaseModel):
    meeting = models.OneToOneField(MeetingOrder, on_delete=models.CASCADE, related_name='link', verbose_name="Встреча")
    link = models.URLField(verbose_name="Ссылка")
    is_send_sms = models.BooleanField(default=False, verbose_name="Смс отправлен")

    class Meta:
        verbose_name = "Ссылка встречи"
        verbose_name_plural = "Ссылки встреч"
        ordering = ('-created_at',)


class MeetingPhone(base_models.BaseModel):
    meeting = models.OneToOneField(MeetingOrder, on_delete=models.CASCADE, related_name='phone', verbose_name="Встреча")
    phone_number = models.CharField(max_length=14, validators=[validate_uz_number], verbose_name="Номер телефона")
    full_name = models.CharField(max_length=255, verbose_name="Полное имя")
    is_send_sms = models.BooleanField(default=False, verbose_name="Смс отправлен")

    class Meta:
        verbose_name = "Телефонная встреча"
        verbose_name_plural = "Телефонные встречи"
        ordering = ('-created_at',)


class MeetingLocation(base_models.BaseModel):
    meeting = models.OneToOneField(MeetingOrder, on_delete=models.CASCADE, related_name='location',
                                   verbose_name="Встреча")
    location_name = models.CharField(max_length=255, verbose_name="Название локации")
    location_url = models.URLField(verbose_name="Локация url")
    is_send_sms = models.BooleanField(default=False, verbose_name="Смс отправлен")

    class Meta:
        verbose_name = "Локация встречи"
        verbose_name_plural = "Локации встреч"
        ordering = ('-created_at',)


@receiver(pre_save, sender=MeetingLink)
@receiver(pre_save, sender=MeetingPhone)
@receiver(pre_save, sender=MeetingLocation)
def track_old_instance(sender, instance, **kwargs):
    if instance.pk:
        old_instance = sender.objects.get(pk=instance.pk)
        instance._old_data = {
            'link': old_instance.link if hasattr(old_instance, 'link') else None,
            'phone_number': old_instance.phone_number if hasattr(old_instance, 'phone_number') else None,
            'location_name': old_instance.location_name if hasattr(old_instance, 'location_name') else None,
            'location_url': old_instance.location_url if hasattr(old_instance, 'location_url') else None,
            'is_send_sms': old_instance.is_send_sms if hasattr(old_instance, 'is_send_sms') else None,
        }


# Signal for sending SMS when is_send_sms is True or data changes
@receiver(post_save, sender=MeetingLink)
@receiver(post_save, sender=MeetingPhone)
@receiver(post_save, sender=MeetingLocation)
def send_meeting_notification(sender, instance, created, **kwargs):
    if created and instance.is_send_sms or instance.is_send_sms and hasattr(instance,
                                                                            '_old_data') and instance._old_data.get(
        'is_send_sms') is False:
        if isinstance(instance, MeetingLink):
            send_notification(f"Onlayn Uchrashuv uchun link {instance.link}  \n{instance.meeting.customer_phone}")
        if isinstance(instance, MeetingPhone):
            send_notification(
                f"Telefon orqali maslahat olish uchun telefon raqam {instance.phone_number}  \n{instance.meeting.customer_phone}")

        if isinstance(instance, MeetingLocation):
            send_notification(
                f"Maslahat olish uchun ofis manzili: {instance.location_name} \nLink:{instance.location_url}  \n{instance.meeting.customer_phone}")


    elif not created and instance.is_send_sms and hasattr(instance, '_old_data'):
        # Send SMS on update if data changed
        if isinstance(instance, MeetingLink) and instance.link != instance._old_data['link']:
            send_notification(f"Uchrashuv linki o'zgardi: {instance.link} \n{instance.meeting.customer_phone}")

        if isinstance(instance, MeetingPhone) and instance.phone_number != instance._old_data['phone_number']:
            send_notification(
                f"Uchrashuv telefon raqami o'zgardi: {instance.phone_number}\n{instance.meeting.customer_phone}")

        if isinstance(instance, MeetingLocation) and instance.location_name != instance._old_data[
            'location_name'] or instance.location_url != instance._old_data['location_url']:
            send_notification(
                f"Uchrashuv manzili o'zgardi: {instance.location_name}\n{instance.meeting.customer_phone}")


class Contacts(base_models.BaseModel):
    full_name = models.CharField(max_length=150, verbose_name="Полное имя")
    email = models.EmailField(null=True, blank=True, verbose_name="Электронная почьта")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    type = models.CharField(max_length=255, null=True, blank=True, verbose_name="Тип")
    message = models.TextField(max_length=1000, verbose_name="Сообщение")
    file = models.FileField(upload_to='contacts/document/', null=True, blank=True, verbose_name="Файл")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ('created_at',)


class Complaint(base_models.BaseModel):
    order_document = models.ForeignKey(DocumentOrder, on_delete=models.CASCADE, verbose_name="Заказ документа")
    complaint = models.TextField(verbose_name="Жалоба")

    def __str__(self):
        return self.complaint[:20]

    class Meta:
        verbose_name = "Жалоба"
        verbose_name_plural = "Жалобы"
        ordering = ('created_at',)


class DocumentOrderPage(base_models.BaseModel):
    is_active = models.BooleanField(default=False, verbose_name="Активен")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Страница заказа документа'
        verbose_name_plural = 'Страница заказов документов'
        ordering = ("-created_at",)


class ServiceEvaluation(base_models.BaseModel):
    meeting = models.OneToOneField(MeetingOrder, on_delete=models.CASCADE, verbose_name="Встреча")

    rating = models.IntegerField(validators=[validate_rating], verbose_name="Рейтинг")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Оценка услуги'
        verbose_name_plural = 'Оценки услуг'
        ordering = ('-created_at',)

@receiver(post_save, sender=DocumentOrder)
@receiver(post_save, sender=MeetingOrder)
@receiver(post_save, sender=Contacts)
def send_telegram_message(sender, instance, created, **kwargs):
    if created:
        if isinstance(instance, DocumentOrder):
            order_type = "Document Order"
            url = f'{settings.CSRF_TRUSTED_ORIGINS[0]}/admin/serviceses/documentorder/{instance.pk}/'
            description = instance.customer_message
            language = "null"
            phone_number = instance.customer_phone

        elif isinstance(instance, MeetingOrder):
            order_type = "Meeting Order " + instance.get_meeting_type_display() if hasattr(instance, 'get_meeting_type_display') else str(instance.meeting_type)
            url = f'{settings.CSRF_TRUSTED_ORIGINS[0]}/admin/serviceses/meetingorder/{instance.pk}/'
            description = instance.short_description if instance.short_description else "Noma'lum"
            language = instance.language if instance.language else "Uz"
            phone_number = instance.customer_phone

        elif isinstance(instance, Contacts):
            order_type = "Contact"
            description = instance.message
            language = "null"
            url = f'{settings.CSRF_TRUSTED_ORIGINS[0]}/admin/serviceses/contacts/{instance.pk}/'
            phone_number = instance.phone

        message = create_message_telegram(
            customer_full_name=getattr(instance, 'customer_full_name', '') or getattr(instance,'full_name'),
            phone_number=phone_number,
            language=language,
            type=f'{order_type}\n',
            description=description,
            url=url
        )

        send_notification(message)