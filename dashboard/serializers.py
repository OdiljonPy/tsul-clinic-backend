from rest_framework import serializers
from ckeditor.fields import RichTextField
from .models import CustomerUser
from base.models import (
    Banner, News, Team, Statistics,
    CustomerOpinion, FAQ, AboutUs, Info,
    OfficeAddress, Services, ServicesCategory,
    AdditionalLinks, Partners
)

from serviceses.models import (
    DocumentCategory, DocumentType, DocumentOrder,
    ReadyDocuments, MeetingOrder, Contacts
)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class BannerAdminSerializer(serializers.ModelSerializer):
    text_uz = serializers.CharField(max_length=150)
    text_ru = serializers.CharField(max_length=150)
    text_en = serializers.CharField(max_length=150)

    class Meta:
        model = Banner
        fields = ['id', 'text', 'text_uz', 'text_ru', "text_en", 'image']


class NewsAdminSerializer(serializers.ModelSerializer):
    title_uz = serializers.CharField(max_length=150)
    title_ru = serializers.CharField(max_length=150)
    title_en = serializers.CharField(max_length=150)

    short_description_uz = serializers.CharField(max_length=225)
    short_description_ru = serializers.CharField(max_length=225)
    short_description_en = serializers.CharField(max_length=225)

    content_uz = RichTextField()
    content_ru = RichTextField()
    content_en = RichTextField()

    class Meta:
        model = News
        fields = ['id', "title", "short_description", 'image', 'content', 'views_count', 'is_published', 'title_uz',
                  'title_ru', 'title_en', 'short_description_uz', 'short_description_ru', 'short_description_en',
                  'content_uz', 'content_ru', 'content_en']


class TeamAdminSerializer(serializers.ModelSerializer):
    full_name_uz = serializers.CharField(max_length=150)
    full_name_ru = serializers.CharField(max_length=150)
    full_name_en = serializers.CharField(max_length=150)

    position_uz = serializers.CharField(max_length=255)
    position_ru = serializers.CharField(max_length=255)
    position_en = serializers.CharField(max_length=255)

    class Meta:
        model = Team
        fields = ['id', 'full_name', 'position', 'image', 'full_name_uz', 'full_name_ru', 'full_name_en', 'position_uz',
                  'position_ru', 'position_en']


class StatisticsAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ['id', 'customers_number', "services_number", "service_indicator"]


class CustomerOpinionAdminSerializer(serializers.ModelSerializer):
    company_name_uz = serializers.CharField(max_length=100)
    company_name_ru = serializers.CharField(max_length=100)
    company_name_en = serializers.CharField(max_length=100)

    position_uz = serializers.CharField(max_length=150)
    position_ru = serializers.CharField(max_length=150)
    position_en = serializers.CharField(max_length=150)

    full_name_uz = serializers.CharField(max_length=150)
    full_name_ru = serializers.CharField(max_length=150)
    full_name_en = serializers.CharField(max_length=150)

    opinion_uz = serializers.CharField(max_length=800)
    opinion_ru = serializers.CharField(max_length=800)
    opinion_en = serializers.CharField(max_length=800)

    class Meta:
        model = CustomerOpinion
        fields = ['id', 'company_name', 'position', 'full_name', 'opinion', 'image', 'company_name_uz',
                  'company_name_ru', "company_name_en", 'position_uz', 'position_ru', 'position_en', 'full_name_uz',
                  'full_name_ru', 'full_name_en', 'opinion_uz', 'opinion_ru', 'opinion_en']


class FAQAdminSerializer(serializers.ModelSerializer):
    question_uz = serializers.CharField(max_length=500)
    question_ru = serializers.CharField(max_length=500)
    question_en = serializers.CharField(max_length=500)

    answer_uz = serializers.CharField(max_length=1000)
    answer_ru = serializers.CharField(max_length=1000)
    answer_en = serializers.CharField(max_length=1000)

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'is_published', 'question_uz', 'question_ru', 'question_en', 'answer_uz',
                  'answer_ru', 'answer_en']


class AboutUsAdminSerializer(serializers.ModelSerializer):
    about_us_uz = RichTextField()
    about_us_ru = RichTextField()
    about_us_en = RichTextField()

    our_goal_uz = serializers.CharField(max_length=500)
    our_goal_ru = serializers.CharField(max_length=500)
    our_goal_en = serializers.CharField(max_length=500)

    class Meta:
        model = AboutUs
        fields = ['id', "about_us", 'our_goal', 'image', 'about_us_uz', 'about_us_ru', 'about_us_en', 'our_goal_uz',
                  'our_goal_ru', 'our_goal_en']


class InfoAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['id', 'youtube', 'instagram', 'twitter', 'linkedin', 'telegram', 'phone_number']


class OfficeAddressAdminSerializer(serializers.ModelSerializer):
    address_name_uz = serializers.CharField(max_length=250)
    address_name_ru = serializers.CharField(max_length=250)
    address_name_en = serializers.CharField(max_length=250)

    class Meta:
        model = OfficeAddress
        fields = ['id', 'info', 'address_name', 'latitude', 'longitude', 'phone', 'address_name_uz', 'address_name_ru',
                  'address_name_en']


class ServicesAdminSerializer(serializers.ModelSerializer):
    name_uz = serializers.CharField(max_length=150)
    name_ru = serializers.CharField(max_length=150)
    name_en = serializers.CharField(max_length=150)

    content_uz = RichTextField()
    content_ru = RichTextField()
    content_en = RichTextField()

    class Meta:
        model = Services
        fields = ['id', 'category', 'image', 'name', 'content', 'name_uz', 'name_ru', 'name_en', 'content_uz',
                  'content_ru', 'content_en']


class ServicesCategoryAdminSerializer(serializers.ModelSerializer):
    name_uz = serializers.CharField(max_length=150)
    name_ru = serializers.CharField(max_length=150)
    name_en = serializers.CharField(max_length=150)

    class Meta:
        model = ServicesCategory
        fields = ['id', 'name', 'name_uz', 'name_ru', 'name_en']


class AdditionalLinksAdminSerializer(serializers.ModelSerializer):
    name_uz = serializers.CharField(max_length=150)
    name_ru = serializers.CharField(max_length=150)
    name_en = serializers.CharField(max_length=150)

    class Meta:
        model = AdditionalLinks
        fields = ['id', 'name', 'url', 'is_published', 'name_uz', 'name_ru', 'name_en']


class PartnersAdminSerializer(serializers.ModelSerializer):
    full_name_uz = serializers.CharField(max_length=150)
    full_name_ru = serializers.CharField(max_length=150)
    full_name_en = serializers.CharField(max_length=150)

    position_uz = serializers.CharField(max_length=255)
    position_ru = serializers.CharField(max_length=255)
    position_en = serializers.CharField(max_length=255)

    class Meta:
        model = Partners
        fields = ['id', 'full_name', 'image', 'position', 'category', 'full_name_uz', 'full_name_ru', 'full_name_en',
                  'position_uz', 'position_ru', 'position_en']


class DocumentCategoryAdminSerializer(serializers.ModelSerializer):
    category_name_uz = serializers.CharField(max_length=150)
    category_name_ru = serializers.CharField(max_length=150)
    category_name_en = serializers.CharField(max_length=150)

    class Meta:
        model = DocumentCategory
        fields = ['id', 'category_name', 'is_active', 'category_name_uz', 'category_name_ru', 'category_name_en']


class DocumentTypeAdminSerializer(serializers.ModelSerializer):
    document_name_uz = serializers.CharField(max_length=150)
    document_name_ru = serializers.CharField(max_length=150)
    document_name_en = serializers.CharField(max_length=150)

    class Meta:
        model = DocumentType
        fields = ['id', 'document_name', 'document_category', 'price', 'is_active', 'document_name_uz',
                  'document_name_ru', 'document_name_en']


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
