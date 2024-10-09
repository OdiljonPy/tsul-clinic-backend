from base import models as base_models
from serviceses import models as services_models
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from exceptions.exception import CustomApiException
from exceptions.error_messages import ErrorCodes
from .serializers import (
    BannerAdminSerializer, NewsAdminSerializer, TeamAdminSerializer, StatisticsAdminSerializer,
    CustomerOpinionAdminSerializer, FAQAdminSerializer, AboutUsAdminSerializer, InfoAdminSerializer,
    OfficeAddressAdminSerializer, ServicesCategoryAdminSerializer, ServicesAdminSerializer,
    AdditionalLinksAdminSerializer, PartnersAdminSerializer, DocumentCategoryAdminSerializer,
    DocumentTypeAdminSerializer, DocumentOrderAdminSerializer, ReadyDocumentsAdminSerializer,
    MeetingOrderAdminSerializer, ContactsAdminSerializer
)


class BannerViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=BannerAdminSerializer(),
        responses={201: BannerAdminSerializer()},
        tags=['Dashboard-Banner']
    )
    def create_banner(self, request):
        data = request.data
        serializer = BannerAdminSerializer(data=data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: BannerAdminSerializer()},
        tags=['Dashboard-Banner']
    )
    def list_banners(self, request):
        banners = base_models.Banner.objects.all()
        serializer = BannerAdminSerializer(banners, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: BannerAdminSerializer()},
        tags=['Dashboard-Banner']
    )
    def retrieve_banner(self, request, pk):
        banner = base_models.Banner.objects.filter(id=pk).first()
        if not banner:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = BannerAdminSerializer(banner)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=BannerAdminSerializer(),
        responses={200: BannerAdminSerializer()},
        tags=['Dashboard-Banner']
    )
    def update_banner(self, request, pk):
        banner = base_models.Banner.objects.filter(id=pk).first()
        if not banner:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = BannerAdminSerializer(banner, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: BannerAdminSerializer()},
        tags=['Dashboard-Banner']
    )
    def delete_banner(self, request, pk):
        banner = base_models.Banner.objects.filter(id=pk).first()
        if not banner:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        banner.delete()
        return Response(data={'result': 'Banner deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class NewsViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=NewsAdminSerializer(),
        responses={201: NewsAdminSerializer()},
        tags=['Dashboard-News']
    )
    def create_news(self, request):
        serializer = NewsAdminSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: NewsAdminSerializer()},
        tags=['Dashboard-News']
    )
    def list_news(self, request):
        news = base_models.News.objects.all()
        serializer = NewsAdminSerializer(news, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: NewsAdminSerializer()},
        tags=['Dashboard-News']
    )
    def retrieve_news(self, request, pk):
        news = base_models.News.objects.filter(id=pk).first()
        if not news:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = NewsAdminSerializer(news)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=NewsAdminSerializer(),
        responses={200: NewsAdminSerializer()},
        tags=['Dashboard-News']
    )
    def update_news(self, request, pk):
        news = base_models.News.objects.filter(id=pk).first()
        if not news:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = NewsAdminSerializer(news, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: NewsAdminSerializer()},
        tags=['Dashboard-News']
    )
    def delete_news(self, request, pk):
        news = base_models.News.objects.filter(id=pk).first()
        if not news:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        news.delete()
        return Response(data={'result': 'News deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class TeamViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=TeamAdminSerializer(),
        responses={201: TeamAdminSerializer()},
        tags=['Dashboard-Team']
    )
    def create_team(self, request):
        serializer = TeamAdminSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: TeamAdminSerializer()},
        tags=['Dashboard-Team']
    )
    def list_teams(self, request):
        teams = base_models.Team.objects.all()
        serializer = TeamAdminSerializer(teams, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: TeamAdminSerializer()},
        tags=['Dashboard-Team']
    )
    def retrieve_team(self, request, pk):
        team = base_models.Team.objects.filter(id=pk).first()
        if not team:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = TeamAdminSerializer(team)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=TeamAdminSerializer(),
        responses={200: TeamAdminSerializer()},
        tags=['Dashboard-Team']
    )
    def update_team(self, request, pk):
        team = base_models.Team.objects.filter(id=pk).first()
        if not team:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = TeamAdminSerializer(team, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: TeamAdminSerializer()},
        tags=['Dashboard-Team']
    )
    def delete_team(self, request, pk):
        team = base_models.Team.objects.filter(id=pk).first()
        if not team:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        team.delete()
        return Response(data={'result': 'Team deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class StatisticsViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=StatisticsAdminSerializer(),
        responses={201: StatisticsAdminSerializer()},
        tags=['Dashboard-Statistics']
    )
    def create_statistics(self, request):
        serializer = StatisticsAdminSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: StatisticsAdminSerializer()},
        tags=['Dashboard-Statistics']
    )
    def list_statistics(self, request):
        statistics = base_models.Statistics.objects.all()
        serializer = StatisticsAdminSerializer(statistics, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: StatisticsAdminSerializer()},
        tags=['Dashboard-Statistics']
    )
    def retrieve_statistics(self, request, pk):
        statistics = base_models.Statistics.objects.filter(id=pk).first()
        if not statistics:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = StatisticsAdminSerializer(statistics)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=StatisticsAdminSerializer(),
        responses={200: StatisticsAdminSerializer()},
        tags=['Dashboard-Statistics']
    )
    def update_statistics(self, request, pk):
        statistics = base_models.Statistics.objects.filter(id=pk).first()
        if not statistics:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = StatisticsAdminSerializer(statistics, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: StatisticsAdminSerializer()},
        tags=['Dashboard-Statistics']
    )
    def delete_statistics(self, request, pk):
        statistics = base_models.Statistics.objects.filter(id=pk).first()
        if not statistics:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        statistics.delete()
        return Response(data={'result': 'Statistics deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class CustomerOpinionViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=CustomerOpinionAdminSerializer(),
        responses={201: CustomerOpinionAdminSerializer()},
        tags=['Dashboard-CustomerOpinion']
    )
    def create_customer_opinion(self, request):
        serializer = CustomerOpinionAdminSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: CustomerOpinionAdminSerializer()},
        tags=['Dashboard-CustomerOpinion']
    )
    def list_customer_opinion(self, request):
        customer_opinions = base_models.CustomerOpinion.objects.all()
        serializer = CustomerOpinionAdminSerializer(customer_opinions, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: CustomerOpinionAdminSerializer()},
        tags=['Dashboard-CustomerOpinion']
    )
    def retrieve_customer_opinion(self, request, pk):
        customer_opinion = base_models.CustomerOpinion.objects.filter(id=pk).first()
        if not customer_opinion:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = CustomerOpinionAdminSerializer(customer_opinion)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=CustomerOpinionAdminSerializer(),
        responses={200: CustomerOpinionAdminSerializer()},
        tags=['Dashboard-CustomerOpinion']
    )
    def update_customer_opinion(self, request, pk):
        customer_opinion = base_models.CustomerOpinion.objects.filter(id=pk).first()
        if not customer_opinion:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = CustomerOpinionAdminSerializer(customer_opinion, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: CustomerOpinionAdminSerializer()},
        tags=['Dashboard-CustomerOpinion']
    )
    def delete_customer_opinion(self, request, pk):
        customer_opinion = base_models.CustomerOpinion.objects.filter(id=pk).first()
        if not customer_opinion:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        customer_opinion.delete()
        return Response(data={'result': 'CustomerOpinion deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class FAQViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=FAQAdminSerializer(),
        responses={201: FAQAdminSerializer()},
        tags=['Dashboard-FAQ']
    )
    def create_faq(self, request):
        serializer = FAQAdminSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: FAQAdminSerializer()},
        tags=['Dashboard-FAQ']
    )
    def list_faq(self, request):
        faqs = base_models.FAQ.objects.all()
        serializer = FAQAdminSerializer(faqs, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: FAQAdminSerializer()},
        tags=['Dashboard-FAQ']
    )
    def retrieve_faq(self, request, pk):
        faq = base_models.FAQ.objects.filter(id=pk).first()
        if not faq:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = FAQAdminSerializer(faq)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=FAQAdminSerializer(),
        responses={200: FAQAdminSerializer()},
        tags=['Dashboard-FAQ']
    )
    def update_faq(self, request, pk):
        faq = base_models.FAQ.objects.filter(id=pk).first()
        if not faq:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = FAQAdminSerializer(faq, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: FAQAdminSerializer()},
        tags=['Dashboard-FAQ']
    )
    def delete_faq(self, request, pk):
        faq = base_models.FAQ.objects.filter(id=pk).first()
        if not faq:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        faq.delete()
        return Response(data={'result': 'FAQ deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class AboutUsViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=AboutUsAdminSerializer(),
        responses={200: AboutUsAdminSerializer()},
        tags=['Dashboard-AboutUs']
    )
    def create_about_us(self, request):
        serializer = AboutUsAdminSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: AboutUsAdminSerializer()},
        tags=['Dashboard-AboutUs']
    )
    def list_about_us(self, request):
        about_us = base_models.AboutUs.objects.all()
        serializer = AboutUsAdminSerializer(about_us, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: AboutUsAdminSerializer()},
        tags=['Dashboard-AboutUs']
    )
    def retrieve_about_us(self, request, pk):
        about_us = base_models.AboutUs.objects.filter(id=pk).first()
        if not about_us:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = AboutUsAdminSerializer(about_us)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=AboutUsAdminSerializer(),
        responses={200: AboutUsAdminSerializer()},
        tags=['Dashboard-AboutUs']
    )
    def update_about_us(self, request, pk):
        about_us = base_models.AboutUs.objects.filter(id=pk).first()
        if not about_us:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = AboutUsAdminSerializer(about_us, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: AboutUsAdminSerializer()},
        tags=['Dashboard-AboutUs']
    )
    def delete_about_us(self, request, pk):
        about_us = base_models.AboutUs.objects.filter(id=pk).first()
        if not about_us:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        about_us.delete()
        return Response(data={'result': 'AboutUs deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class InfoViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=InfoAdminSerializer(),
        responses={200: InfoAdminSerializer()},
        tags=['Dashboard-Info']
    )
    def create_info(self, request):
        serializer = InfoAdminSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: InfoAdminSerializer()},
        tags=['Dashboard-Info']
    )
    def list_info(self, request):
        info = base_models.Info.objects.all()
        serializer = InfoAdminSerializer(info, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: InfoAdminSerializer()},
        tags=['Dashboard-Info']
    )
    def retrieve_info(self, request, pk):
        info = base_models.Info.objects.filter(id=pk).first()
        if not info:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = InfoAdminSerializer(info)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=InfoAdminSerializer(),
        responses={200: InfoAdminSerializer()},
        tags=['Dashboard-Info']
    )
    def update_info(self, request, pk):
        info = base_models.Info.objects.filter(id=pk).first()
        if not info:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = InfoAdminSerializer(info, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: InfoAdminSerializer()},
        tags=['Dashboard-Info']
    )
    def delete_info(self, request, pk):
        info = base_models.Info.objects.filter(id=pk).first()
        if not info:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        info.delete()
        return Response(data={'result': 'Info deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class OfficeAddressViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=OfficeAddressAdminSerializer(),
        responses={200: OfficeAddressAdminSerializer()},
        tags=['Dashboard-OfficeAddresses']
    )
    def create_office_address(self, request):
        serializer = OfficeAddressAdminSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: OfficeAddressAdminSerializer()},
        tags=['Dashboard-OfficeAddresses']
    )
    def list_office_addresses(self, request):
        office_addresses = base_models.OfficeAddress.objects.all()
        serializer = OfficeAddressAdminSerializer(office_addresses, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: OfficeAddressAdminSerializer()},
        tags=['Dashboard-OfficeAddresses']
    )
    def retrieve_office_address(self, request, pk):
        office_address = base_models.OfficeAddress.objects.filter(id=pk).first()
        if not office_address:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = OfficeAddressAdminSerializer(office_address)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=OfficeAddressAdminSerializer(),
        responses={200: OfficeAddressAdminSerializer()},
        tags=['Dashboard-OfficeAddress']
    )
    def update_office_address(self, request, pk):
        office_address = base_models.OfficeAddress.objects.filter(id=pk).first()
        if not office_address:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = OfficeAddressAdminSerializer(office_address, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: OfficeAddressAdminSerializer()},
        tags=['Dashboard-OfficeAddress']
    )
    def delete_office_address(self, request, pk):
        office_address = base_models.OfficeAddress.objects.filter(id=pk).first()
        if not office_address:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        office_address.delete()
        return Response(data={'result': 'Office address deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class ServicesCategoryViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=ServicesCategoryAdminSerializer(),
        responses={200: ServicesCategoryAdminSerializer()},
        tags=['Dashboard-ServicesCategories']
    )
    def create_service_category(self, request):
        serializer = ServicesCategoryAdminSerializer(data=request.data)
        if serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: ServicesCategoryAdminSerializer()},
        tags=['Dashboard-ServicesCategories']
    )
    def list_service_categories(self, request):
        service_categories = base_models.ServicesCategory.objects.all()
        serializer = ServicesCategoryAdminSerializer(service_categories, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: ServicesCategoryAdminSerializer()},
        tags=['Dashboard-ServicesCategories']
    )
    def retrieve_service_category(self, request, pk):
        service_category = base_models.ServicesCategory.objects.filter(id=pk).first()
        if not service_category:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = ServicesCategoryAdminSerializer(service_category)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=ServicesCategoryAdminSerializer(),
        responses={200: ServicesCategoryAdminSerializer()},
        tags=['Dashboard-ServicesCategories']
    )
    def update_service_category(self, request, pk):
        service_category = base_models.ServicesCategory.objects.filter(id=pk).first()
        if not service_category:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = ServicesCategoryAdminSerializer(service_category, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: ServicesCategoryAdminSerializer()},
        tags=['Dashboard-ServicesCategories']
    )
    def delete_service_category(self, request, pk):
        service_category = base_models.ServicesCategory.objects.filter(id=pk).first()
        if not service_category:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        service_category.delete()
        return Response(data={'result': 'Service category deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class ServicesViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=ServicesAdminSerializer(),
        responses={200: ServicesAdminSerializer()},
        tags=['Dashboard-Services']
    )
    def create_service(self, request):
        serializer = ServicesAdminSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: ServicesAdminSerializer()},
        tags=['Dashboard-Services']
    )
    def list_services(self, request):
        services = base_models.Services.objects.all()
        serializer = ServicesAdminSerializer(services, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: ServicesAdminSerializer()},
        tags=['Dashboard-Services']
    )
    def retrieve_service(self, request, pk):
        service = base_models.Services.objects.filter(id=pk).first()
        if not service:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = ServicesAdminSerializer(service)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=ServicesAdminSerializer(),
        responses={200: ServicesAdminSerializer()},
        tags=['Dashboard-Services']
    )
    def update_service(self, request, pk):
        service = base_models.Services.objects.filter(id=pk).first()
        if not service:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = ServicesAdminSerializer(service, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: ServicesAdminSerializer()},
        tags=['Dashboard-Services']
    )
    def delete_service(self, request, pk):
        service = base_models.Services.objects.filter(id=pk).first()
        if not service:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        service.delete()


class AdditionalLinksViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=AdditionalLinksAdminSerializer(),
        responses={201: AdditionalLinksAdminSerializer()},
        tags=['Dashboard-AdditionalLinks']
    )
    def create_additional_links(self, request):
        serializer = AdditionalLinksAdminSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: AdditionalLinksAdminSerializer()},
        tags=['Dashboard-AdditionalLinks']
    )
    def list_additional_links(self, request):
        additional_links = base_models.AdditionalLinks.objects.all()
        serializer = AdditionalLinksAdminSerializer(additional_links, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: AdditionalLinksAdminSerializer()},
        tags=['Dashboard-AdditionalLinks']
    )
    def retrieve_additional_link(self, request, pk):
        additional_link = base_models.AdditionalLinks.objects.filter(id=pk).first()
        if not additional_link:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = AdditionalLinksAdminSerializer(additional_link)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=AdditionalLinksAdminSerializer(),
        responses={200: AdditionalLinksAdminSerializer()},
        tags=['Dashboard-AdditionalLinks']
    )
    def update_additional_link(self, request, pk):
        additional_link = base_models.AdditionalLinks.objects.filter(id=pk).first()
        if not additional_link:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = AdditionalLinksAdminSerializer(additional_link, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: AdditionalLinksAdminSerializer()},
        tags=['Dashboard-AdditionalLinks']
    )
    def delete_additional_link(self, request, pk):
        additional_link = base_models.AdditionalLinks.objects.filter(id=pk).first()
        if not additional_link:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        additional_link.delete()
        return Response(data={'result': 'Additional Links deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class PartnersViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=PartnersAdminSerializer(),
        responses={201: PartnersAdminSerializer()},
        tags=['Dashboard-Partners']
    )
    def create_partner(self, request):
        serializer = PartnersAdminSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: PartnersAdminSerializer()},
        tags=['Dashboard-Partners']
    )
    def list_partners(self, request):
        partners = base_models.Partners.objects.all()
        serializer = PartnersAdminSerializer(partners, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: PartnersAdminSerializer()},
        tags=['Dashboard-Partners']
    )
    def retrieve_partner(self, request, pk):
        partner = base_models.Partners.objects.filter(id=pk).first()
        if not partner:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = PartnersAdminSerializer(partner)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=PartnersAdminSerializer(),
        responses={200: PartnersAdminSerializer()},
        tags=['Dashboard-Partners']
    )
    def update_partner(self, request, pk):
        partner = base_models.Partners.objects.filter(id=pk).first()
        if not partner:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = PartnersAdminSerializer(partner, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: PartnersAdminSerializer()},
        tags=['Dashboard-Partners']
    )
    def delete_partner(self, request, pk):
        partner = base_models.Partners.objects.filter(id=pk).first()
        if not partner:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        partner.delete()
        return Response(data={'result': 'Partner deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class DocumentCategoryViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=DocumentCategoryAdminSerializer(),
        responses={201: DocumentCategoryAdminSerializer()},
        tags=['Dashboard-DocumentCategory']
    )
    def create_document_category(self, request):
        serializer = DocumentCategoryAdminSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: DocumentCategoryAdminSerializer()},
        tags=['Dashboard-DocumentCategory']
    )
    def list_document_category(self, request):
        document_categories = services_models.DocumentCategory.objects.all()
        serializer = DocumentCategoryAdminSerializer(document_categories, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: DocumentCategoryAdminSerializer()},
        tags=['Dashboard-DocumentCategory']
    )
    def retrieve_document_category(self, request, pk):
        document_category = services_models.DocumentCategory.objects.filter(id=pk).first()
        if not document_category:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = DocumentCategoryAdminSerializer(document_category)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=DocumentCategoryAdminSerializer(),
        responses={200: DocumentCategoryAdminSerializer()},
        tags=['Dashboard-DocumentCategory']
    )
    def update_document_category(self, request, pk):
        document_category = services_models.DocumentCategory.objects.filter(id=pk).first()
        if not document_category:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = DocumentCategoryAdminSerializer(document_category, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: DocumentCategoryAdminSerializer()},
        tags=['Dashboard-DocumentCategory']
    )
    def delete_document_category(self, request, pk):
        document_category = services_models.DocumentCategory.objects.filter(id=pk).first()
        if not document_category:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        document_category.delete()
        return Response(
            data={'result': 'Document category deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class DocumentTypeViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=DocumentTypeAdminSerializer(),
        responses={201: DocumentTypeAdminSerializer()},
        tags=['Dashboard-DocumentType']
    )
    def create_document_type(self, request):
        serializer = DocumentTypeAdminSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: DocumentTypeAdminSerializer()},
        tags=['Dashboard-DocumentType']
    )
    def list_document_type(self, request):
        document_types = services_models.DocumentType.objects.all()
        serializer = DocumentTypeAdminSerializer(document_types, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: DocumentTypeAdminSerializer()},
        tags=['Dashboard-DocumentType']
    )
    def retrieve_document_type(self, request, pk):
        document_type = services_models.DocumentType.objects.filter(id=pk).first()
        if not document_type:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = DocumentTypeAdminSerializer(document_type)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=DocumentTypeAdminSerializer(),
        responses={200: DocumentTypeAdminSerializer()},
        tags=['Dashboard-DocumentType']
    )
    def update_document_type(self, request, pk):
        document_type = services_models.DocumentType.objects.filter(id=pk).first()
        if not document_type:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = DocumentTypeAdminSerializer(document_type, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: DocumentTypeAdminSerializer()},
        tags=['Dashboard-DocumentType']
    )
    def delete_document_type(self, request, pk):
        document_type = services_models.DocumentType.objects.filter(id=pk).first()
        if not document_type:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        document_type.delete()
        return Response(data={'result': 'Document type deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class DocumentOrderViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=DocumentOrderAdminSerializer(),
        responses={201: DocumentOrderAdminSerializer()},
        tags=['Dashboard-DocumentOrder']
    )
    def create_document_order(self, request):
        serializer = DocumentOrderAdminSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: DocumentOrderAdminSerializer()},
        tags=['Dashboard-DocumentOrder']
    )
    def list_document_order(self, request):
        document_orders = services_models.DocumentOrder.objects.all()
        serializer = DocumentOrderAdminSerializer(document_orders, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: DocumentOrderAdminSerializer()},
        tags=['Dashboard-DocumentOrder']
    )
    def retrieve_document_order(self, request, pk):
        document_order = services_models.DocumentOrder.objects.filter(id=pk).first()
        if not document_order:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = DocumentOrderAdminSerializer(document_order)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=DocumentOrderAdminSerializer(),
        responses={200: DocumentOrderAdminSerializer()},
    )
    def update_document_order(self, request, pk):
        document_order = services_models.DocumentOrder.objects.filter(id=pk).first()
        if not document_order:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = DocumentOrderAdminSerializer(document_order, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: DocumentOrderAdminSerializer()},
        tags=['Dashboard-DocumentOrder']
    )
    def delete_document_order(self, request, pk):
        document_order = services_models.DocumentOrder.objects.filter(id=pk).first()
        if not document_order:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        document_order.delete()
        return Response(data={'result': 'Document order deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class ReadyDocumentsViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=ReadyDocumentsAdminSerializer(),
        responses={201: ReadyDocumentsAdminSerializer()},
        tags=['Dashboard-ReadyDocuments']
    )
    def create_ready_document(self, request):
        serializer = ReadyDocumentsAdminSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: ReadyDocumentsAdminSerializer()},
        tags=['Dashboard-ReadyDocuments']
    )
    def list_ready_document(self, request):
        ready_documents = services_models.ReadyDocuments.objects.all()
        serializer = ReadyDocumentsAdminSerializer(ready_documents, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: ReadyDocumentsAdminSerializer()},
        tags=['Dashboard-ReadyDocuments']
    )
    def retrieve_ready_document(self, request, pk):
        ready_document = services_models.ReadyDocuments.objects.filter(id=pk).first()
        if not ready_document:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = ReadyDocumentsAdminSerializer(ready_document)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=ReadyDocumentsAdminSerializer(),
        responses={200: ReadyDocumentsAdminSerializer()},
        tags=['Dashboard-ReadyDocuments']
    )
    def update_ready_document(self, request, pk):
        ready_document = services_models.ReadyDocuments.objects.filter(id=pk).first()
        if not ready_document:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = ReadyDocumentsAdminSerializer(ready_document, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: ReadyDocumentsAdminSerializer()},
        tags=['Dashboard-ReadyDocuments']
    )
    def delete_ready_document(self, request, pk):
        ready_document = services_models.ReadyDocuments.objects.filter(id=pk).first()
        if not ready_document:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        ready_document.delete()
        return Response(data={'result': 'Ready document deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class MeetingOrderViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=MeetingOrderAdminSerializer(),
        responses={201: MeetingOrderAdminSerializer()},
        tags=['Dashboard-MeetingOrder']
    )
    def create_meeting_order(self, request):
        serializer = MeetingOrderAdminSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: MeetingOrderAdminSerializer()},
        tags=['Dashboard-MeetingOrder']
    )
    def list_meeting_order(self, request):
        meeting_orders = services_models.MeetingOrder.objects.all()
        serializer = MeetingOrderAdminSerializer(meeting_orders, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: MeetingOrderAdminSerializer()},
        tags=['Dashboard-MeetingOrder']
    )
    def retrieve_meeting_order(self, request, pk):
        meeting_order = services_models.MeetingOrder.objects.filter(id=pk).first()
        if not meeting_order:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = MeetingOrderAdminSerializer(meeting_order)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=MeetingOrderAdminSerializer(),
        responses={200: MeetingOrderAdminSerializer()},
        tags=['Dashboard-MeetingOrder']
    )
    def update_meeting_order(self, request, pk):
        meeting_order = services_models.MeetingOrder.objects.filter(id=pk).first()
        if not meeting_order:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = MeetingOrderAdminSerializer(meeting_order, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: MeetingOrderAdminSerializer()},
        tags=['Dashboard-MeetingOrder']
    )
    def delete_meeting_order(self, request, pk):
        meeting_order = services_models.MeetingOrder.objects.filter(id=pk).first()
        if not meeting_order:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        meeting_order.delete()
        return Response(data={'result': 'Meeting order deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class ContactsViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=ContactsAdminSerializer(),
        responses={201: ContactsAdminSerializer()},
        tags=['Dashboard-Contacts']
    )
    def create_contacts(self, request):
        serializer = ContactsAdminSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: ContactsAdminSerializer()},
        tags=['Dashboard-Contacts']
    )
    def list_contacts(self, request):
        contacts = services_models.Contacts.objects.all()
        serializer = ContactsAdminSerializer(contacts, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: ContactsAdminSerializer()},
        tags=['Dashboard-Contacts']
    )
    def retrieve_contacts(self, request, pk):
        contacts = services_models.Contacts.objects.filter(id=pk).first()
        if not contacts:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = ContactsAdminSerializer(contacts)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=ContactsAdminSerializer(),
        responses={200: ContactsAdminSerializer()},
        tags=['Dashboard-Contacts']
    )
    def update_contacts(self, request, pk):
        contacts = services_models.Contacts.objects.filter(id=pk).first()
        if not contacts:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = ContactsAdminSerializer(contacts, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: ContactsAdminSerializer()},
        tags=['Dashboard-Contacts']
    )
    def delete_contacts(self, request, pk):
        contacts = services_models.Contacts.objects.filter(id=pk).first()
        if not contacts:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        contacts.delete()
        return Response(data={'result': 'Contact deleted successfully', 'ok': True}, status=status.HTTP_200_OK)
