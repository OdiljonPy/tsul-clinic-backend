from django.contrib import admin

from .models import DocumentOrder, MeetingOrder, Contacts, ReadyDocuments, Complaint, MeetingLink, MeetingPhone, \
    MeetingLocation


# admin.site.unregister(Theme)
class ComplaintAdminTabularInline(admin.TabularInline):
    model = Complaint
    extra = 0


# class DocumentTypeAdminTabularInline(admin.TabularInline):
#     model = DocumentType
#     extra = 1


class ReadyDocumentsTabularInline(admin.TabularInline):
    model = ReadyDocuments
    extra = 1


class MeetingLinkTabularInline(admin.TabularInline):
    model = MeetingLink
    extra = 1


class MeetingPhoneTabularInline(admin.TabularInline):
    model = MeetingPhone
    extra = 1


class MeetingLocationTabularInline(admin.TabularInline):
    model = MeetingLocation
    extra = 1


# @admin.register(DocumentCategory)
# class DocumentCategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'category_name', 'is_active')
#     list_display_links = ('id', 'category_name')
#     search_fields = ('id', 'category_name')
#     list_filter = ('is_active',)
#     inlines = (DocumentTypeAdminTabularInline,)
#
#
# @admin.register(DocumentType)
# class DocumentTypeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'document_name', 'document_category', 'is_active')
#     list_display_links = ('id', 'document_name')
#     search_fields = ('id', 'document_name')
#     list_filter = ('is_active',)

# def save_model(self, request, obj, form, change):
# if obj.price:
#     message_create(get_message(MessageEnumCode.PAYMENT_RECEIVED), item1=obj.)


@admin.register(DocumentOrder)
class DocumentOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_number', 'customer_full_name', 'status')
    list_display_links = ('id', 'order_number', 'customer_full_name')
    search_fields = ('id', 'order_number', 'customer_full_name')
    list_filter = ('status',)
    inlines = (ReadyDocumentsTabularInline, ComplaintAdminTabularInline)
    readonly_fields = ('order_number',)


@admin.register(MeetingOrder)
class MeetingOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_number', 'customer_full_name', 'customer_phone', 'meeting_time')
    list_display_links = ('id', 'order_number', 'customer_full_name')
    search_fields = ('id', 'order_number', 'customer_full_name', 'customer_phone')
    list_filter = ('meeting_type', 'meeting_time', 'meeting_status')
    readonly_fields = ('order_number',)

    def get_inline_instances(self, request, obj=None):
        # Get the base inline instances, don't forget this line!
        inline_instances = super().get_inline_instances(request, obj)

        if obj:
            if obj.meeting_type == 1:
                inline_instances.append(MeetingLinkTabularInline(self.model, self.admin_site))
            elif obj.meeting_type == 0:
                inline_instances.append(MeetingPhoneTabularInline(self.model, self.admin_site))
            elif obj.meeting_type == 2:
                inline_instances.append(MeetingLocationTabularInline(self.model, self.admin_site))

        return inline_instances


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'email', 'type')
    list_display_links = ('id', 'full_name', 'phone')
    search_fields = ('id', 'full_name', 'phone', 'email')
    list_filter = ('type',)
