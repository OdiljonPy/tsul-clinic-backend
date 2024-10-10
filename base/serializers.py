from django.conf import settings
from rest_framework import serializers

from exceptions.error_messages import ErrorCodes
from exceptions.exception import CustomApiException
from .models import (
    News,
    Team,
    Statistics,
    CustomerOpinion,
    FAQ,
    AboutUs,
    Info,
    OfficeAddress,
    ServicesCategory,
    Services,
    AdditionalLinks,
    Banner,
    Partners, FAQCategory
)


class NewsSerializer(serializers.ModelSerializer):
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
        fields = ('id', 'title', 'short_description', 'image', 'content', 'created_at')


class TeamSerializer(serializers.ModelSerializer):
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
        fields = ('id', 'full_name', 'position', 'image', 'is_volunteer')


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ('id', 'customers_number', 'services_number', 'service_indicator')


class CustomerOpinionSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        self.fields['full_name'] = serializers.CharField(source=f'full_name_{language}')
        self.fields['opinion'] = serializers.CharField(source=f'opinion_{language}')

    class Meta:
        model = CustomerOpinion
        fields = ('id', 'full_name', 'opinion', 'created_at', 'video')


class FAQCategorySerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        self.fields['name'] = serializers.CharField(source=f'name_{language}')

    class Meta:
        model = FAQCategory
        fields = ['id', 'name']


class FAQSerializer(serializers.ModelSerializer):
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
        fields = ('id', 'question', 'answer', 'created_at')


class AboutUsSerializer(serializers.ModelSerializer):
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
        fields = ('id', 'about_us', 'our_goal', 'image')


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('id', 'youtube', 'instagram', 'twitter', 'linkedin', 'telegram', 'phone_number')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['office_address'] = OfficeAddressSerializer(instance.office_address.all(), many=True,
                                                         context=self.context).data
        return data


class OfficeAddressSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        self.fields['address_name'] = serializers.CharField(source=f'address_name_{language}')

    class Meta:
        model = OfficeAddress
        fields = ('id', 'address_name', 'latitude', 'longitude')


class ServicesCategorySerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        self.fields['name'] = serializers.CharField(source=f'name_{language}')

    class Meta:
        model = ServicesCategory
        fields = ('id', 'name')


class ServicesSerializer(serializers.ModelSerializer):
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
        fields = ('id', 'name', 'category', 'image', 'content')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        if instance.category:
            category_name = getattr(instance.category, f'name_{language}', '')
            data['category'] = category_name or ''
        else:
            data['category'] = ''

        return data


class AdditionalLinksSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        self.fields['name'] = serializers.CharField(source=f'name_{language}')

    class Meta:
        model = AdditionalLinks
        fields = ('id', 'name', 'url')


class BannerSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        self.fields['text'] = serializers.CharField(source=f'text_{language}')

    class Meta:
        model = Banner
        fields = ('id', 'text', 'image')


class PaginatorSerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, default=1)
    page_size = serializers.IntegerField(required=False, default=10)

    def validate(self, attrs):
        page = attrs.get('page')
        page_size = attrs.get('page_size')
        if page_size < 0 or page < 0:
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message='Page or page size is invalid')
        return attrs


class PartnersSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        language = 'ru'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        self.fields['company_name'] = serializers.CharField(source=f'full_name_{language}')

    class Meta:
        model = Partners
        fields = ('id', 'company_name', 'image')
