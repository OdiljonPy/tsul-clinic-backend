from django.urls import path

from .views import NewsViewSet, TeamViewSet, BaseViewSet, PartnersViewSet

urlpatterns = [
    path('news/', NewsViewSet.as_view({'get': 'list'}), name='news'),
    path('news/<int:pk>/', NewsViewSet.as_view({'get': 'retrieve'}), name='news_detail'),
    path('news/popular/', NewsViewSet.as_view({'get': 'popular_news'}), name='popular_news'),
    path('team/', TeamViewSet.as_view({'get': 'list'}), name='time'),
    path('partners/', PartnersViewSet.as_view({'get': 'list'}), name='partners'),
    path('statistics/', BaseViewSet.as_view({'get': 'get_statistics'}), name='statistics'),
    path('opinion/', BaseViewSet.as_view({'get': 'list_opinion'}), name='opinion'),
    path('faq/category/', BaseViewSet.as_view({'get': 'list_faq_category'}), name='faq_category'),
    path('faq/category/<int:pk>/', BaseViewSet.as_view({'get': 'faq_category_detail'}), name='faq_category_detail'),
    path('about/', BaseViewSet.as_view({'get': 'get_about_us'}), name='about'),
    path('info/', BaseViewSet.as_view({'get': 'get_info'}), name='info'),
    path('services/category/', BaseViewSet.as_view({'get': 'list_services_category'}), name='services_category'),
    path('services/', BaseViewSet.as_view({'get': 'list_services'}), name='services'),
    path('services/<int:pk>/', BaseViewSet.as_view({'get': 'retrieve'}), name='services_detail'),
    path('links/', BaseViewSet.as_view({'get': 'list_addition_link'}), name='links'),
    path('banners/', BaseViewSet.as_view({'get': 'list_banner'}), name='banners'),
    path('projects/', BaseViewSet.as_view({'get': 'get_projects'}), name='projects'),
    path('achievement/', BaseViewSet.as_view({'get': 'list_achievement'}), name='list_achievement'),
    path('manual/', BaseViewSet.as_view({'get': 'get_manual_links'}), name='list_achievement'),

]
