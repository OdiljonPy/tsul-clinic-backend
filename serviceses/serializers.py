from rest_framework import serializers
from django.conf import settings
from .models import (
    DocumentOrder,
    MeetingOrder,
    Contacts, ReadyDocuments, Complaint, ServiceEvaluation
)


# class DocumentCategorySerializer(serializers.ModelSerializer):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         request = self.context.get('request')
#         language = 'ru'
#         if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
#             language = request.META.get('HTTP_ACCEPT_LANGUAGE')
#
#         self.fields['category_name'] = serializers.CharField(source=f'category_name_{language}')
#
#     class Meta:
#         model = DocumentCategory
#         fields = ('id', 'category_name')
#
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data['document_type'] = DocumentTypeSerializer(instance.documenttype_set.filter(is_active=True), many=True,
#                                                        context=self.context).data
#         return data


# class DocumentTypeSerializer(serializers.ModelSerializer):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         request = self.context.get('request')
#         language = 'ru'
#         if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
#             language = request.META.get('HTTP_ACCEPT_LANGUAGE')
#
#         self.fields['document_name'] = serializers.CharField(source=f'document_name_{language}')
#
#     class Meta:
#         model = DocumentType
#         fields = ('id', 'document_name', 'document_category', 'price')


class ReadyDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadyDocuments
        fields = ('id', 'document_name', 'document')


class DocumentOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentOrder
        fields = ('id', 'order_number', 'document_type', 'customer_full_name', 'customer_phone',
                  'customer_email', 'customer_message', 'status', 'price', 'created_at', 'file')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['ready_documents'] = ReadyDocumentsSerializer(instance.readydocuments_set.all(), many=True,
                                                           context=self.context).data
        return data

    def create(self, validated_data):
        validated_data.pop('order_number', None)
        validated_data.pop('price', None)
        validated_data.pop('status', None)
        # Create and return the DocumentOrder instance
        return super().create(validated_data)


class MeetingOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingOrder
        fields = (
            'id', 'order_number', 'language', 'short_description', 'customer_full_name', 'customer_phone',
            'customer_email',
            'meeting_type')

    def create(self, validated_data):
        validated_data.pop('order_number', None)

        return super().create(validated_data)


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('id', 'full_name', 'email', 'phone', 'message', 'type', 'file')


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ['id', 'complaint', 'order_document']


class ServiceEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceEvaluation
        fields = ['id', 'meeting', 'rating', 'description']
