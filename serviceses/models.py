from django.db import models
from abstract_models import base_models

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
    category_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name


class DocumentType(base_models.BaseModel):
    document_name = models.CharField(max_length=150)
    document_category = models.ForeignKey(DocumentCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.document_name


class DocumentOrder(base_models.BaseModel):
    order_number = models.CharField(max_length=150, blank=True, null=True)
    document_category = models.ForeignKey(DocumentCategory, on_delete=models.SET_NULL, null=True)
    document_type = models.ForeignKey(DocumentType, on_delete=models.SET_NULL, null=True)
    customer_full_name = models.CharField(max_length=250)
    customer_phone = models.CharField(max_length=20)
    customer_email = models.EmailField(null=True, blank=True)
    customer_message = models.TextField(max_length=1000)
    status = models.IntegerField(default=0, choices=DOCUMENT_ORDER_STATUS)

    def __str__(self):
        return self.customer_full_name


class MeetingOrder(base_models.BaseModel):
    order_number = models.CharField(max_length=150, blank=True, null=True)
    customer_full_name = models.CharField(max_length=150)
    customer_phone = models.CharField(max_length=20)
    customer_email = models.EmailField(null=True, blank=True)
    meeting_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    meeting_status = models.IntegerField(default=0, choices=MEETING_ORDER_STATUS)
    meeting_type = models.IntegerField(choices=MEETING_ORDER_TYPES)
    meeting_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.customer_full_name


class Contacts(base_models.BaseModel):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    type = models.ForeignKey(DocumentCategory, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.full_name
