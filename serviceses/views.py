from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from yaml import serialize

from exceptions.error_messages import ErrorCodes
from exceptions.exception import CustomApiException
from .models import DocumentOrder, DocumentOrderPage, MeetingOrder, ServiceEvaluation
from .serializers import (
    DocumentOrderSerializer,
    MeetingOrderSerializer,
    ContactsSerializer, ComplaintSerializer, ServiceEvaluationSerializer
)


class DocumentOrderViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Create order for documents',
        request_body=DocumentOrderSerializer,
        responses={201: DocumentOrderSerializer()},
        tags=['DocumentOrder'],
    )
    def create(self, request):
        check_page = DocumentOrderPage.objects.order_by('-created_at').first()
        if getattr(check_page, 'is_active', False) is False:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = DocumentOrderSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        order = serializer.save()

        return Response({'response': DocumentOrderSerializer(order).data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary='Check Document order page',
        responses={200: 'response: True/False'},
        tags=['DocumentOrder Page'],
    )
    def get_check_page(self, request):
        check_page = DocumentOrderPage.objects.order_by('-created_at').first()
        return Response({'response': getattr(check_page, 'is_active', False), 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Check order for documents',
        responses={200: DocumentOrderSerializer()},
        tags=['DocumentOrder'],
    )
    def check_document(self, request, document_id):
        document = DocumentOrder.objects.filter(order_number=document_id).first()
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


class ComplaintViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=ComplaintSerializer,
        responses={201: ComplaintSerializer()},
        tags=['Complaints'],
        operation_summary='Create complaint',
        operation_description='Create complaint, DocumentOrder id for pk',
    )
    def create(self, request, pk):
        data = request.data
        data['order_document'] = pk
        serializer = ComplaintSerializer(data=data, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response({'response': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)


class EvaluationViewSet(ViewSet):
    @swagger_auto_schema(
        responses={200: "response:True/False"},
        tags=['Evaluation'],
    )
    def check_evaluation(self, request, pk):
        return Response({"response": ServiceEvaluation.objects.filter(meeting_id=pk).exists(), 'ok': True},
                        status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=ServiceEvaluationSerializer,
        responses={201: ServiceEvaluationSerializer()},
        tags=['Evaluation'],
    )
    def create(self, request, pk):
        meeting = MeetingOrder.objects.filter(pk=pk).first()
        if not meeting:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = ServiceEvaluationSerializer(data={**request.data, 'meeting':pk},
                                                 context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response({'response': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)
