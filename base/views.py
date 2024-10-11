from collections import defaultdict

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

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
    ServicesCategory,
    Services,
    AdditionalLinks,
    Banner,
    Partners,
    CHOICE_PARTNERS,
    FAQCategory,
    Projects, Achievements, ManualWebsite
)
from .repository.get_news import get_news
from .serializers import (
    PaginatorSerializer,
    NewsSerializer,
    TeamSerializer,
    StatisticsSerializer,
    CustomerOpinionSerializer,
    FAQSerializer,
    AboutUsSerializer,
    InfoSerializer,
    ServicesCategorySerializer,
    ServicesSerializer,
    AdditionalLinksSerializer,
    BannerSerializer,
    PartnersSerializer, FAQCategorySerializer, ProjectsSerializer, AchievementsImages, AchievementsSerializer
)


class NewsViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='News list',
        manual_parameters=[
            openapi.Parameter(
                name='page', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='Page'),
            openapi.Parameter(
                name='page_size', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='Page size'),
        ],
        responses={200: NewsSerializer(many=True)},
        tags=['News'],
    )
    def list(self, request):
        serializer_params = PaginatorSerializer(data=request.query_params)
        if not serializer_params.is_valid():
            raise CustomApiException(ErrorCodes.VALIDATION_FAILED, message=serializer_params.errors)
        news = News.objects.filter(is_published=True)
        response = get_news(response=news, context={'request': request},
                            page_size=serializer_params.validated_data.get('page_size'),
                            page=serializer_params.validated_data.get('page'))
        return Response({'response': response, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='News details',
        responses={200: NewsSerializer()},
        tags=['News'],
    )
    def retrieve(self, request, pk):
        news = News.objects.filter(id=pk, is_published=True).first()
        if not news:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        news.views_count += 1
        news.save()
        return Response({'response': NewsSerializer(news, context={'request': request}).data, 'ok': True},
                        status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Popular news lists',
        responses={200: NewsSerializer(many=True)},
        tags=['News'],
    )
    def popular_news(self, request):
        news = News.objects.filter(is_published=True).order_by('-created_at').order_by('-views_count')[:5]
        return Response({'response': NewsSerializer(news, context={'request': request}, many=True).data, 'ok': True},
                        status=status.HTTP_200_OK)


class TeamViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Team list',
        responses={200: TeamSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter(
                name='type', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING, description='volunteer')
        ],
        tags=['Team'],
    )
    def list(self, request):
        type = request.query_params.get('type')
        if  type and type == 'volunteer':
            teams = Team.objects.filter(is_volunteer=True)
        else:
            teams = Team.objects.filter(is_volunteer=False)
        return Response({'response': TeamSerializer(teams, context={'request': request}, many=True).data, 'ok': True},
                        status=status.HTTP_200_OK)


class PartnersViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Partner list',
        responses={200: PartnersSerializer(many=True)},
        tags=['Partner'],
    )
    def list(self, request):
        partners = Partners.objects.all()
        serialized_data = PartnersSerializer(partners, context={'request': request}, many=True).data

        # Group by category using defaultdict
        grouped_data = defaultdict(list)
        for partner in serialized_data:
            grouped_data[partner['category']].append(partner)

        # Convert defaultdict to a standard dict and ensure all categories are included
        response_data = {str(category): grouped_data.get(category, []) for category, _ in CHOICE_PARTNERS}

        return Response({'response': response_data, 'ok': True}, status=status.HTTP_200_OK)


class BaseViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Statistics',
        responses={200: StatisticsSerializer()},
        tags=['Base'],
    )
    def get_statistics(self, request):
        statistics = Statistics.objects.order_by('-created_at').first()
        return Response({'response': StatisticsSerializer(statistics, context={'request': request}).data, 'ok': True},
                        status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Opinions lists',
        responses={200: CustomerOpinionSerializer(many=True)},
        tags=['Base'],
    )
    def list_opinion(self, request):
        opinions = CustomerOpinion.objects.all().order_by('-created_at')
        return Response({'response': CustomerOpinionSerializer(opinions, many=True, context={'request': request}).data,
                         'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='FAQ category list',
        operation_description="FAQ category list",
        responses={200: FAQCategorySerializer(many=True)},
        tags=['Base'],
    )
    def list_faq_category(self, request):
        faq_category = FAQCategory.objects.all()
        serializer = FAQCategorySerializer(faq_category, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="FAQ category detail",
        operation_description='FAQ category detail',
        responses={200: FAQCategorySerializer()},
        tags=['Base'],
    )
    def faq_category_detail(self, request, pk):
        faq_category = FAQCategory.objects.filter(id=pk).first()
        if not faq_category:
            raise CustomApiException(error_code=ErrorCodes.NOT_FOUND, message='FAQ category not found')

        serializer = FAQCategorySerializer(faq_category, context={'request': request}).data
        serializer['faq_list'] = FAQSerializer(faq_category.faq_category.all(), many=True,
                                               context={'request': request}).data
        return Response(data={'result': serializer, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Frequently Asked Question list',
        responses={200: FAQSerializer(many=True)},
        tags=['Base'],
    )
    def list_faq(self, request):
        faq = FAQ.objects.filter(is_published=True).order_by('-created_at')
        return Response({'response': FAQSerializer(faq, many=True, context={'request': request}).data, 'ok': True},
                        status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='About Us',
        responses={200: AboutUsSerializer()},
        tags=['Base'],
    )
    def get_about_us(self, request):
        about_us = AboutUs.objects.order_by('-created_at').first()
        return Response({'response': AboutUsSerializer(about_us, context={'request': request}).data, 'ok': True},
                        status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='INFO',
        responses={200: InfoSerializer()},
        tags=['Base'],
    )
    def get_info(self, request):
        info = Info.objects.order_by('-created_at').first()
        return Response({'response': InfoSerializer(info, context={'request': request}).data, 'ok': True},
                        status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Services Category list',
        responses={200: ServicesCategorySerializer(many=True)},
        tags=['Base'],
    )
    def list_services_category(self, request):
        services_category = ServicesCategory.objects.all()
        return Response(
            {'response': ServicesCategorySerializer(services_category, many=True, context={'request': request}).data,
             'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Services list',
        responses={200: ServicesSerializer(many=True)},
        tags=['Base'],
    )
    def list_services(self, request):
        services = Services.objects.all()
        return Response({'response': ServicesSerializer(services, many=True, context={'request': request}).data,
                         'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Services details',
        responses={200: ServicesSerializer()},
        tags=['Base'],
    )
    def retrieve(self, request, pk):
        services = Services.objects.filter(id=pk).first()
        if not services:
            raise CustomApiException(ErrorCodes.NOT_FOUND)
        return Response({'response': ServicesSerializer(services, context={'request': request}).data, 'ok': True},
                        status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Additional links list',
        responses={200: AdditionalLinksSerializer(many=True)},
        tags=['Base'],
    )
    def list_addition_link(self, request):
        links = AdditionalLinks.objects.filter(is_published=True)
        return Response(
            {'response': AdditionalLinksSerializer(links, many=True, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Banner list',
        responses={200: BannerSerializer(many=True)},
        tags=['Base'],
    )
    def list_banner(self, request):
        banner = Banner.objects.order_by('-created_at')[:4]
        return Response(
            {'response': BannerSerializer(banner, many=True, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Project list',
        responses={200: ProjectsSerializer(many=True)},
        tags=['Base'],
    )
    def get_projects(self, request):
        projects = Projects.objects.all()
        return Response(
            {'response': ProjectsSerializer(projects, many=True, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Achievements list',
        responses={200: AchievementsSerializer(many=True)},
        tags=['Base'],
    )
    def list_achievement(self, request):
        achievements = Achievements.objects.all()
        return Response({'response': AchievementsSerializer(achievements, many=True, context={'request': request}).data,
                         'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Manual link',
        responses={200: 'response:youtube_url'},
        tags=['Base'],
    )
    def get_manual_links(self, request):
        link = ManualWebsite.objects.order_by('-created_at').first()
        return Response({'response': getattr(link, 'youtube_link', ''), 'ok': True}, status=status.HTTP_200_OK)
