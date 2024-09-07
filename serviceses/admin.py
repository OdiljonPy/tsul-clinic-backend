from django.contrib import admin
from .models import DocumentCategory, DocumentType, DocumentOrder, MeetingOrder, Contacts


@admin.register(DocumentCategory)
class DocumentCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'is_active')
    list_display_links = ('id', 'category_name')
    search_fields = ('id', 'category_name')
    list_filter = ('is_active',)


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'document_name', 'document_category', 'is_active')
    list_display_links = ('id', 'document_name')
    search_fields = ('id', 'document_name')
    list_filter = ('is_active',)


@admin.register(DocumentOrder)
class DocumentOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_number', 'customer_full_name', 'document_category', 'status')
    list_display_links = ('id', 'order_number', 'customer_full_name')
    search_fields = ('id', 'order_number', 'customer_full_name')
    list_filter = ('status',)


@admin.register(MeetingOrder)
class MeetingOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_number', 'customer_full_name', 'customer_phone', 'meeting_time')
    list_display_links = ('id', 'order_number', 'customer_full_name')
    search_fields = ('id', 'order_number', 'customer_full_name', 'customer_phone')
    list_filter = ('meeting_type', 'meeting_time', 'meeting_status')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'email', 'type')
    list_display_links = ('id', 'full_name', 'phone')
    search_fields = ('id', 'full_name', 'phone', 'email')
    list_filter = ('type',)
