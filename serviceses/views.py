from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from exceptions.error_messages import ErrorCodes
from exceptions.exception import CustomApiException
from .models import DocumentCategory, DocumentOrder
from .serializers import (
    DocumentCategorySerializer,
    DocumentOrderSerializer,
    MeetingOrderSerializer,
    ContactsSerializer
)


class DocumentCategoryViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Get Document Categories',
        responses={200: DocumentCategorySerializer(many=True)},
        tags=['DocumentCategory'],
    )
    def list(self, request):
        categories = DocumentCategory.objects.filter(is_active=True, documenttype__isnull=False)
        return Response(
            {"response": DocumentCategorySerializer(categories, many=True, context={"request": request}).data,
             'ok': True},
            status=status.HTTP_200_OK)


class DocumentOrderViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Create order for documents',
        request_body=DocumentOrderSerializer,
        responses={201: DocumentOrderSerializer()},
        tags=['DocumentOrder'],
    )
    def create(self, request):
        serializer = DocumentOrderSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response({'response': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary='Check order for documents',
        responses={200: DocumentOrderSerializer()},
        tags=['DocumentOrder'],
    )
    def check_document(self, request, document_id):
        document = DocumentOrder.objects.filter(order_number=document_id).filter()
        return Response({'response': DocumentOrderSerializer(document, context={'request': request}).data, 'ok': True},
                        status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Create order for meeting',
        request_body=MeetingOrderSerializer,
        responses={201: MeetingOrderSerializer()},
        tags=['DocumentOrder'],
    )
    def create_meeting(self, request):
        serializer = MeetingOrderSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response({'response': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)


class ContactsViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Create contact',
        request_body=ContactsSerializer,
        responses={201: ContactsSerializer()},
        tags=['Contacts'],
    )
    def create(self, request):
        serializer = ContactsSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response({'response': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)
