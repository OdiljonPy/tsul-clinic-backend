from django.contrib import admin
from .models import DocumentCategory, DocumentType, DocumentOrder, MeetingOrder, Contacts, ReadyDocuments
from utils.notification_messages import get_message, MessageEnumCode
from utils.send_notifications import message_create


class DocumentTypeAdminTabularInline(admin.TabularInline):
    model = DocumentType
    extra = 1


class ReadyDocumentsTabularInline(admin.TabularInline):
    model = ReadyDocuments
    extra = 1


@admin.register(DocumentCategory)
class DocumentCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'is_active')
    list_display_links = ('id', 'category_name')
    search_fields = ('id', 'category_name')
    list_filter = ('is_active',)
    inlines = (DocumentTypeAdminTabularInline,)


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'document_name', 'document_category', 'is_active')
    list_display_links = ('id', 'document_name')
    search_fields = ('id', 'document_name')
    list_filter = ('is_active',)

    # def save_model(self, request, obj, form, change):
    # if obj.price:
    #     message_create(get_message(MessageEnumCode.PAYMENT_RECEIVED), item1=obj.)


@admin.register(DocumentOrder)
class DocumentOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_number', 'customer_full_name', 'document_category', 'status')
    list_display_links = ('id', 'order_number', 'customer_full_name')
    search_fields = ('id', 'order_number', 'customer_full_name')
    list_filter = ('status',)
    inlines = (ReadyDocumentsTabularInline,)

    def save_model(self, request, obj, form, change):
        if obj.status == 1:
            message_create(message=get_message(MessageEnumCode.PAYMENT_RECEIVED), item1=obj.order_number)
        # if not change:
        print(obj.document_category.category_name)
        print(obj.document_category.is_active)
        # message_create(message=get_message(MessageEnumCode.CREATE_DOCUMENT), item1=obj.order_number)
        super().save_model(request, obj, form, change)


@admin.register(MeetingOrder)
class MeetingOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_number', 'customer_full_name', 'customer_phone', 'meeting_time')
    list_display_links = ('id', 'order_number', 'customer_full_name')
    search_fields = ('id', 'order_number', 'customer_full_name', 'customer_phone')
    list_filter = ('meeting_type', 'meeting_time', 'meeting_status')

    def save_model(self, request, obj, form, change):
        print('Change', change)
        print(obj.__dict__)
        if not change:
            if obj.meeting_type == 0:
                message_create(message=get_message(MessageEnumCode.PHONE_MEETING_TIME),
                               item1=obj.order_number, item2=obj.meeting_time)
            elif obj.meeting_type == 1:
                message_create(message=get_message(MessageEnumCode.VIDEO_MEETING_TIME),
                               item1=obj.order_number, item2=obj.meeting_time)
            elif obj.meeting_type == 2:
                message_create(message=get_message(MessageEnumCode.MEETING_TIME),
                               item1=obj.order_number, item2=obj.meeting_time)
        if obj.meeting_status == 1:
            message_create(message=get_message(MessageEnumCode.CREATE_MEETING), item1=obj.order_number)
        super().save_model(request, obj, form, change)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'email', 'type')
    list_display_links = ('id', 'full_name', 'phone')
    search_fields = ('id', 'full_name', 'phone', 'email')
    list_filter = ('type',)
