from rest_framework import serializers

from .models import (
    DocumentCategory,
    DocumentType,
    DocumentOrder,
    MeetingOrder,
    Contacts, ReadyDocuments
)


class DocumentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentCategory
        fields = ('id', 'category_name')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['document_type'] = DocumentTypeSerializer(instance.documenttype_set.all(), many=True,
                                                       context=self.context).data
        return data


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ('id', 'document_name', 'document_category', 'price')


class ReadyDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadyDocuments
        fields = ('id', 'document_name', 'document')


class DocumentOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentOrder
        fields = ('id', 'order_number', 'document_category', 'document_type', 'customer_full_name', 'customer_phone',
                  'customer_email', 'customer_message', 'status', 'created_at')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['ready_documents'] = ReadyDocumentsSerializer(instance.readydocuments_set.all(), many=True,
                                                           context=self.context).data
        return data


class MeetingOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingOrder
        fields = ('id', 'order_number', 'customer_full_name', 'customer_phone', 'customer_email', 'meeting_type')


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('id', 'full_name', 'email', 'phone', 'message', 'type')
