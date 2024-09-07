from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from exceptions.error_messages import ErrorCodes
from exceptions.exception import CustomApiException
from .models import DocumentCategory
from .serializers import DocumentCategorySerializer, DocumentTypeSerializer, DocumentOrderSerializer, \
    MeetingOrderSerializer, ContactsSerializer


class DocumentCategoryViewSet(ViewSet):
    @swagger_auto_schema(
        responses={200: DocumentCategorySerializer(many=True)},
        tags=['DocumentCategory'],
    )
    def list(self, request):
        categories = DocumentCategory.objects.filter(is_active=True)
        return Response(
            {"result": DocumentTypeSerializer(categories, many=True, context={"request": request}).data, 'ok': True},
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
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary='Create order for meeting',
        request_body=DocumentOrderSerializer,
        responses={201: DocumentOrderSerializer()},
        tags=['DocumentOrder'],
    )
    def create_meeting(self, request):
        serializer = MeetingOrderSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ContactsViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=ContactsSerializer,
        responses={201: ContactsSerializer()},
        tags=['Contacts'],
    )
    def create(self, request):
        serializer = ContactsSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
