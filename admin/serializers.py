from rest_framework import serializers
from django.conf import settings

from base.models import Banner, News, Team, Statistics, CustomerOpinion, FAQ, AboutUs, Info, OfficeAddress, Services, \
    ServicesCategory, AdditionalLinks, Partners

from serviceses.models import DocumentCategory, DocumentType, DocumentOrder, ReadyDocuments, MeetingOrder, Contacts


class BannerAdminSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        self.fields['text'] = serializers.CharField(source=f'text_{language}')

    class Meta:
        model = Banner
        fields = ['id', 'text', 'image']


class NewsAdminSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        self.fields['title'] = serializers.CharField(source=f'title_{language}')
        self.fields['short_description'] = serializers.CharField(source=f'short_description_{language}')
        self.fields['content'] = serializers.CharField(source=f'content_{language}')

    class Meta:
        model = News
        fields = ['id', "title", "short_description", 'image', 'content', 'views_count', 'is_published']


class TeamAdminSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        self.fields['full_name'] = serializers.CharField(source=f'full_name_{language}')
        self.fields['position'] = serializers.CharField(source=f'position_{language}')

    class Meta:
        model = Team
        fields = ['id', 'full_name', 'position', 'image']


class StatisticsAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ['id', 'customers_number', "services_number", "service_indicator"]


class CustomerOpinionAdminSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        self.fields['company_name'] = serializers.CharField(source=f'company_name_{language}')
        self.fields['position'] = serializers.CharField(source=f'position_{language}')
        self.fields['full_name'] = serializers.CharField(source=f'full_name_{language}')
        self.fields['opinion'] = serializers.CharField(source=f'opinion_{language}')

    class Meta:
        model = CustomerOpinion
        fields = ['id', 'company_name', 'position', 'full_name', 'opinion', 'image']


class FAQAdminSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        self.fields['question'] = serializers.CharField(source=f'question_{language}')
        self.fields['answer'] = serializers.CharField(source=f'answer_{language}')

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'is_published']


class AboutUsAdminSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        self.fields['about_us'] = serializers.CharField(source=f'about_us_{language}')
        self.fields['our_goal'] = serializers.CharField(source=f'our_goal_{language}')

    class Meta:
        model = AboutUs
        field = ['id', "about_us", 'our_goal', 'image']


class InfoAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['id', 'youtube', 'instagram', 'twitter', 'linkedin', 'telegram', 'phone_number']


class OfficeAddressAdminSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        self.fields['address_name'] = serializers.CharField(source=f'address_name_{language}')

    class Meta:
        model = OfficeAddress
        fields = ['id', 'info', 'address_name', 'latitude', 'longitude', 'phone']


class ServicesAdminSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        self.fields['name'] = serializers.CharField(source=f'name_{language}')
        self.fields['content'] = serializers.CharField(source=f'content_{language}')

    class Meta:
        model = Services
        fields = ['id', 'category', 'image', 'name', 'content']


class ServicesCategoryAdminSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        self.fields['name'] = serializers.CharField(source=f'name_{language}')

    class Meta:
        model = ServicesCategory
        fields = ['id', 'name']


class AdditionalLinksAdminSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        self.fields['name'] = serializers.CharField(source=f'name_{language}')

    class Meta:
        model = AdditionalLinks
        fields = ['id', 'name', 'url', 'is_published']


class PartnersAdminSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        self.fields['full_name'] = serializers.CharField(source=f'full_name_{language}')
        self.fields['position'] = serializers.CharField(source=f'position_{language}')

    class Meta:
        model = Partners
        fields = ['id', 'full_name', 'image', 'position', 'category']


class DocumentCategoryAdminSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        self.fields['category_name'] = serializers.CharField(source=f'category_name_{language}')

    class Meta:
        model = DocumentCategory
        fields = ['id', 'category_name', 'is_active']


class DocumentTypeAdminSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        self.fields['document_name'] = serializers.CharField(source=f'document_name_{language}')

    class Meta:
        model = DocumentType
        fields = ['id', 'document_name', 'document_category', 'price', 'is_active']


class DocumentOrderAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentOrder
        fields = ['id', 'order_number', 'document_category', 'price', 'document_type', 'customer_full_name',
                  'customer_phone', 'customer_email', "customer_message", 'status']


class ReadyDocumentsAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadyDocuments
        fields = ['id', "document_order", 'document_name', 'document']


class MeetingOrderAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingOrder
        fields = ['id', 'order_number', 'customer_full_name', 'customer_phone', 'customer_email', 'meeting_status',
                  'meeting_price', 'meeting_type', 'meeting_time']


class ContactsAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id', "full_name", 'phone', 'email', 'type', 'message']
