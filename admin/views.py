from base import models as base_models
from serviceses import models as services_models
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from exceptions.exception import CustomApiException
from exceptions.error_messages import ErrorCodes

BannerSerializer = ...
NewsSerializer = ...
TeamSerializer = ...
StatisticsSerializer = ...
CustomerOpinionSerializer = ...
FAQSerializer = ...
AboutUsSerializer = ...
InfoSerializer = ...
OfficeAddressSerializer = ...
ServicesCategorySerializer = ...
ServicesSerializer = ...
AdditionalLinksSerializer = ...
PartnersSerializer = ...
DocumentCategorySerializer = ...
DocumentTypeSerializer = ...
DocumentOrderSerializer = ...
ReadyDocumentsSerializer = ...
MeetingOrderSerializer = ...
ContactsSerializer = ...


class BannerViewSet(ViewSet):
    @swagger_auto_schema()
    def create_banner(self, request):
        data = request.data
        serializer = BannerSerializer(data=data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema()
    def list_banners(self, request):
        banners = base_models.Banner.objects.all()
        serializer = BannerSerializer(banners, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def retrieve_banner(self, request, pk):
        banner = base_models.Banner.objects.filter(id=pk).first()
        if not banner:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = BannerSerializer(banner)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def update_banner(self, request, pk):
        banner = base_models.Banner.objects.filter(id=pk).first()
        if not banner:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = BannerSerializer(banner, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def delete_banner(self, request, pk):
        banner = base_models.Banner.objects.filter(id=pk).first()
        if not banner:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        banner.delete()
        return Response(data={'result': 'Banner deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class NewsViewSet(ViewSet):
    @swagger_auto_schema()
    def create_news(self, request):
        serializer = NewsSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema()
    def list_news(self, request):
        news = base_models.News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def retrieve_news(self, request, pk):
        news = base_models.News.objects.filter(id=pk).first()
        if not news:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = NewsSerializer(news)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def update_news(self, request, pk):
        news = base_models.News.objects.filter(id=pk).first()
        if not news:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = NewsSerializer(news, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def delete_news(self, request, pk):
        news = base_models.News.objects.filter(id=pk).first()
        if not news:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        news.delete()
        return Response(data={'result': 'News deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class TeamViewSet(ViewSet):
    @swagger_auto_schema()
    def create_team(self, request):
        serializer = TeamSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema()
    def list_teams(self, request):
        teams = base_models.Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def retrieve_team(self, request, pk):
        team = base_models.Team.objects.filter(id=pk).first()
        if not team:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = TeamSerializer(team)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def update_team(self, request, pk):
        team = base_models.Team.objects.filter(id=pk).first()
        if not team:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = TeamSerializer(team, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def delete_team(self, request, pk):
        team = base_models.Team.objects.filter(id=pk).first()
        if not team:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        team.delete()
        return Response(data={'result': 'Team deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class StatisticsViewSet(ViewSet):
    @swagger_auto_schema()
    def create_statistics(self, request):
        serializer = StatisticsSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema()
    def list_statistics(self, request):
        statistics = base_models.Statistics.objects.all()
        serializer = StatisticsSerializer(statistics, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def retrieve_statistics(self, request, pk):
        statistics = base_models.Statistics.objects.filter(id=pk).first()
        if not statistics:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = StatisticsSerializer(statistics)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def update_statistics(self, request, pk):
        statistics = base_models.Statistics.objects.filter(id=pk).first()
        if not statistics:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = StatisticsSerializer(statistics, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def delete_statistics(self, request, pk):
        statistics = base_models.Statistics.objects.filter(id=pk).first()
        if not statistics:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        statistics.delete()
        return Response(data={'result': 'Statistics deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class CustomerOpinionViewSet(ViewSet):
    @swagger_auto_schema()
    def create_customer_opinion(self, request):
        serializer = CustomerOpinionSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema()
    def list_customer_opinion(self, request):
        customer_opinions = base_models.CustomerOpinion.objects.all()
        serializer = CustomerOpinionSerializer(customer_opinions, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def retrieve_customer_opinion(self, request, pk):
        customer_opinion = base_models.CustomerOpinion.objects.filter(id=pk).first()
        if not customer_opinion:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = CustomerOpinionSerializer(customer_opinion)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def update_customer_opinion(self, request, pk):
        customer_opinion = base_models.CustomerOpinion.objects.filter(id=pk).first()
        if not customer_opinion:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = CustomerOpinionSerializer(customer_opinion, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def delete_customer_opinion(self, request, pk):
        customer_opinion = base_models.CustomerOpinion.objects.filter(id=pk).first()
        if not customer_opinion:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        customer_opinion.delete()
        return Response(data={'result': 'CustomerOpinion deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class FAQViewSet(ViewSet):
    @swagger_auto_schema()
    def create_faq(self, request):
        serializer = FAQSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema()
    def list_faq(self, request):
        faqs = base_models.FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def retrieve_faq(self, request, pk):
        faq = base_models.FAQ.objects.filter(id=pk).first()
        if not faq:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = FAQSerializer(faq)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def update_faq(self, request, pk):
        faq = base_models.FAQ.objects.filter(id=pk).first()
        if not faq:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = FAQSerializer(faq, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def delete_faq(self, request, pk):
        faq = base_models.FAQ.objects.filter(id=pk).first()
        if not faq:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        faq.delete()
        return Response(data={'result': 'FAQ deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class AboutUsViewSet(ViewSet):
    @swagger_auto_schema()
    def create_about_us(self, request):
        serializer = AboutUsSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema()
    def list_about_us(self, request):
        about_us = base_models.AboutUs.objects.all()
        serializer = AboutUsSerializer(about_us, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def retrieve_about_us(self, request, pk):
        about_us = base_models.AboutUs.objects.filter(id=pk).first()
        if not about_us:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = AboutUsSerializer(about_us)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def update_about_us(self, request, pk):
        about_us = base_models.AboutUs.objects.filter(id=pk).first()
        if not about_us:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = AboutUsSerializer(about_us, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def delete_about_us(self, request, pk):
        about_us = base_models.AboutUs.objects.filter(id=pk).first()
        if not about_us:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        about_us.delete()
        return Response(data={'result': 'AboutUs deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class InfoViewSet(ViewSet):
    @swagger_auto_schema()
    def create_info(self, request):
        serializer = InfoSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema()
    def list_info(self, request):
        info = base_models.Info.objects.all()
        serializer = InfoSerializer(info, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def retrieve_info(self, request, pk):
        info = base_models.Info.objects.filter(id=pk).first()
        if not info:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = InfoSerializer(info)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def update_info(self, request, pk):
        info = base_models.Info.objects.filter(id=pk).first()
        if not info:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = InfoSerializer(info, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def delete_info(self, request, pk):
        info = base_models.Info.objects.filter(id=pk).first()
        if not info:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        info.delete()
        return Response(data={'result': 'Info deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class OfficeAddressViewSet(ViewSet):
    @swagger_auto_schema()
    def create_office_address(self, request):
        from base.serializers import OfficeAddressSerializer
        serializer = OfficeAddressSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema()
    def list_office_addresses(self, request):
        office_addresses = base_models.OfficeAddress.objects.all()
        serializer = OfficeAddressSerializer(office_addresses, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def retrieve_office_address(self, request, pk):
        office_address = base_models.OfficeAddress.objects.filter(id=pk).first()
        if not office_address:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = OfficeAddressSerializer(office_address)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def update_office_address(self, request, pk):
        office_address = base_models.OfficeAddress.objects.filter(id=pk).first()
        if not office_address:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = OfficeAddressSerializer(office_address, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def delete_office_address(self, request, pk):
        office_address = base_models.OfficeAddress.objects.filter(id=pk).first()
        if not office_address:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        office_address.delete()
        return Response(data={'result': 'Office address deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class ServicesCategoryViewSet(ViewSet):
    @swagger_auto_schema()
    def create_service_category(self, request):
        serializer = ServicesCategorySerializer(data=request.data)
        if serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema()
    def list_service_categories(self, request):
        service_categories = base_models.ServicesCategory.objects.all()
        serializer = ServicesCategorySerializer(service_categories, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def retrieve_service_category(self, request, pk):
        service_category = base_models.ServicesCategory.objects.filter(id=pk).first()
        if not service_category:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = ServicesCategorySerializer(service_category)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def update_service_category(self, request, pk):
        service_category = base_models.ServicesCategory.objects.filter(id=pk).first()
        if not service_category:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = ServicesCategorySerializer(service_category, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def delete_service_category(self, request, pk):
        service_category = base_models.ServicesCategory.objects.filter(id=pk).first()
        if not service_category:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        service_category.delete()
        return Response(data={'result': 'Service category deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class ServicesViewSet(ViewSet):
    @swagger_auto_schema()
    def create_service(self, request):
        serializer = ServicesSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema()
    def list_services(self, request):
        services = base_models.Services.objects.all()
        serializer = ServicesSerializer(services, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def retrieve_service(self, request, pk):
        service = base_models.Services.objects.filter(id=pk).first()
        if not service:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = ServicesSerializer(service)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def update_service(self, request, pk):
        service = base_models.Services.objects.filter(id=pk).first()
        if not service:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = ServicesSerializer(service, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def delete_service(self, request, pk):
        service = base_models.Services.objects.filter(id=pk).first()
        if not service:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        service.delete()


class AdditionalLinksViewSet(ViewSet):
    @swagger_auto_schema()
    def create_additional_links(self, request):
        serializer = AdditionalLinksSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema()
    def list_additional_links(self, request):
        additional_links = base_models.AdditionalLinks.objects.all()
        serializer = AdditionalLinksSerializer(additional_links, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def retrieve_additional_link(self, request, pk):
        additional_link = base_models.AdditionalLinks.objects.filter(id=pk).first()
        if not additional_link:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = AdditionalLinksSerializer(additional_link)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def update_additional_link(self, request, pk):
        additional_link = base_models.AdditionalLinks.objects.filter(id=pk).first()
        if not additional_link:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = AdditionalLinksSerializer(additional_link, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def delete_additional_link(self, request, pk):
        additional_link = base_models.AdditionalLinks.objects.filter(id=pk).first()
        if not additional_link:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        additional_link.delete()
        return Response(data={'result': 'Additional Links deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class PartnersViewSet(ViewSet):
    @swagger_auto_schema()
    def create_partner(self, request):
        serializer = PartnersSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema()
    def list_partners(self, request):
        partners = base_models.Partners.objects.all()
        serializer = PartnersSerializer(partners, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def retrieve_partner(self, request, pk):
        partner = base_models.Partners.objects.filter(id=pk).first()
        if not partner:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = PartnersSerializer(partner)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def update_partner(self, request, pk):
        partner = base_models.Partners.objects.filter(id=pk).first()
        if not partner:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = PartnersSerializer(partner, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def delete_partner(self, request, pk):
        partner = base_models.Partners.objects.filter(id=pk).first()
        if not partner:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        partner.delete()
        return Response(data={'result': 'Partner deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class DocumentCategoryViewSet(ViewSet):
    @swagger_auto_schema()
    def create_document_category(self, request):
        serializer = DocumentCategorySerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema()
    def list_document_category(self, request):
        document_categories = services_models.DocumentCategory.objects.all()
        serializer = DocumentCategorySerializer(document_categories, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def retrieve_document_category(self, request, pk):
        document_category = services_models.DocumentCategory.objects.filter(id=pk).first()
        if not document_category:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = DocumentCategorySerializer(document_category)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def update_document_category(self, request, pk):
        document_category = services_models.DocumentCategory.objects.filter(id=pk).first()
        if not document_category:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = DocumentCategorySerializer(document_category, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def delete_document_category(self, request, pk):
        document_category = services_models.DocumentCategory.objects.filter(id=pk).first()
        if not document_category:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        document_category.delete()
        return Response(
            data={'result': 'Document category deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class DocumentTypeViewSet(ViewSet):
    @swagger_auto_schema()
    def create_document_type(self, request):
        serializer = DocumentTypeSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema()
    def list_document_type(self, request):
        document_types = services_models.DocumentType.objects.all()
        serializer = DocumentTypeSerializer(document_types, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def retrieve_document_type(self, request, pk):
        document_type = services_models.DocumentType.objects.filter(id=pk).first()
        if not document_type:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = DocumentTypeSerializer(document_type)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def update_document_type(self, request, pk):
        document_type = services_models.DocumentType.objects.filter(id=pk).first()
        if not document_type:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = DocumentTypeSerializer(document_type, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def delete_document_type(self, request, pk):
        document_type = services_models.DocumentType.objects.filter(id=pk).first()
        if not document_type:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        document_type.delete()
        return Response(data={'result': 'Document type deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class DocumentOrderViewSet(ViewSet):
    @swagger_auto_schema()
    def create_document_order(self, request):
        serializer = DocumentOrderSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema()
    def list_document_order(self, request):
        document_orders = services_models.DocumentOrder.objects.all()
        serializer = DocumentOrderSerializer(document_orders, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def retrieve_document_order(self, request, pk):
        document_order = services_models.DocumentOrder.objects.filter(id=pk).first()
        if not document_order:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = DocumentOrderSerializer(document_order)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def update_document_order(self, request, pk):
        document_order = services_models.DocumentOrder.objects.filter(id=pk).first()
        if not document_order:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = DocumentOrderSerializer(document_order, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def delete_document_order(self, request, pk):
        document_order = services_models.DocumentOrder.objects.filter(id=pk).first()
        if not document_order:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        document_order.delete()
        return Response(data={'result': 'Document order deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class ReadyDocumentsViewSet(ViewSet):
    @swagger_auto_schema()
    def create_ready_document(self, request):
        serializer = ReadyDocumentsSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema()
    def list_ready_document(self, request):
        ready_documents = services_models.ReadyDocuments.objects.all()
        serializer = ReadyDocumentsSerializer(ready_documents, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def retrieve_ready_document(self, request, pk):
        ready_document = services_models.ReadyDocuments.objects.filter(id=pk).first()
        if not ready_document:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = ReadyDocumentsSerializer(ready_document)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def update_ready_document(self, request, pk):
        ready_document = services_models.ReadyDocuments.objects.filter(id=pk).first()
        if not ready_document:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = ReadyDocumentsSerializer(ready_document, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def delete_ready_document(self, request, pk):
        ready_document = services_models.ReadyDocuments.objects.filter(id=pk).first()
        if not ready_document:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        ready_document.delete()
        return Response(data={'result': 'Ready document deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class MeetingOrderViewSet(ViewSet):
    @swagger_auto_schema()
    def create_meeting_order(self, request):
        serializer = MeetingOrderSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema()
    def list_meeting_order(self, request):
        meeting_orders = services_models.MeetingOrder.objects.all()
        serializer = MeetingOrderSerializer(meeting_orders, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def retrieve_meeting_order(self, request, pk):
        meeting_order = services_models.MeetingOrder.objects.filter(id=pk).first()
        if not meeting_order:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = MeetingOrderSerializer(meeting_order)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def update_meeting_order(self, request, pk):
        meeting_order = services_models.MeetingOrder.objects.filter(id=pk).first()
        if not meeting_order:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = MeetingOrderSerializer(meeting_order, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def delete_meeting_order(self, request, pk):
        meeting_order = services_models.MeetingOrder.objects.filter(id=pk).first()
        if not meeting_order:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        meeting_order.delete()
        return Response(data={'result': 'Meeting order deleted successfully', 'ok': True}, status=status.HTTP_200_OK)


class ContactsViewSet(ViewSet):
    @swagger_auto_schema()
    def create_contacts(self, request):
        serializer = ContactsSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema()
    def list_contacts(self, request):
        contacts = services_models.Contacts.objects.all()
        serializer = ContactsSerializer(contacts, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def retrieve_contacts(self, request, pk):
        contacts = services_models.Contacts.objects.filter(id=pk).first()
        if not contacts:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        serializer = ContactsSerializer(contacts)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def update_contacts(self, request, pk):
        contacts = services_models.Contacts.objects.filter(id=pk).first()
        if not contacts:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        serializer = ContactsSerializer(contacts, data=request.data, partial=True)
        if not serializer.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema()
    def delete_contacts(self, request, pk):
        contacts = services_models.Contacts.objects.filter(id=pk).first()
        if not contacts:
            raise CustomApiException(ErrorCodes.INVALID_INPUT)
        contacts.delete()
        return Response(data={'result': 'Contact deleted successfully', 'ok': True}, status=status.HTTP_200_OK)
