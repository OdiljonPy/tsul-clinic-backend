from django.urls import path
from . import views

urlpatterns = [
    path('banners/', views.BannerViewSet.as_view({'post': 'create_banner', 'get': 'list_banners'})),
    path('banners/<int:pk>/', views.BannerViewSet.as_view(
        {'get': 'retrieve_banner', 'patch': 'update_banner', 'delete': 'delete_banner'})),

    path('news/', views.NewsViewSet.as_view({'post': 'create_news', 'get': 'list_news'})),
    path('news/<int:pk>/', views.NewsViewSet.as_view(
        {'get': 'retrieve_news', 'patch': 'update_news', 'delete': 'delete_news'})),

    path('team/', views.TeamViewSet.as_view({'post': 'create_team', 'get': 'list_teams'})),
    path('team/<int:pk>/', views.TeamViewSet.as_view(
        {'get': 'retrieve_team', 'patch': 'update_team', 'delete': 'delete_team'})),

    path('statistics/', views.StatisticsViewSet.as_view({'post': 'create_statistics', 'get': 'list_statistics'})),
    path('statistics/<int:pk>/', views.StatisticsViewSet.as_view(
        {'get': 'retrieve_statistics', 'patch': 'update_statistics', 'delete': 'delete_statistics'})),

    path('customer/', views.CustomerOpinionViewSet.as_view(
        {'post': 'create_customer_opinion', 'get': 'list_customer_opinion'})),
    path('customer/<int:pk>/', views.CustomerOpinionViewSet.as_view(
        {'get': 'retrieve_customer_opinion', 'patch': 'update_customer_opinion', 'delete': 'delete_customer_opinion'})),

    path('faq/', views.FAQViewSet.as_view({'post': 'create_faq', 'get': 'list_faq'})),
    path('faq/<int:pk>/', views.FAQViewSet.as_view(
        {'get': 'retrieve_faq', 'patch': 'update_faq', 'delete': 'delete_faq'})),

    path('about/', views.AboutUsViewSet.as_view({'post': 'create_about_us', 'get': 'list_about_us'})),
    path('about/<int:pk>/', views.AboutUsViewSet.as_view(
        {'get': 'retrieve_about_us', 'patch': 'update_about_us', 'delete': 'delete_about_us'})),

    path('info/', views.InfoViewSet.as_view({'post': 'create_info', 'get': 'list_info'})),
    path('info/<int:pk>/', views.InfoViewSet.as_view(
        {'get': 'retrieve_info', 'patch': 'update_info', 'delete': 'delete_info'})),

    path('office/address/', views.OfficeAddressViewSet.as_view(
        {'post': 'create_office_address', 'get': 'list_office_addresses'})),
    path('office/address/<int:pk>/', views.OfficeAddressViewSet.as_view(
        {'get': 'retrieve_office_address', 'patch': 'update_office_address', 'delete': 'delete_office_address'})),

    path('services/category/', views.ServicesCategoryViewSet.as_view(
        {'post': 'create_service_category', 'get': 'list_service_categories'})),
    path('services/category/<int:pk>/', views.ServicesCategoryViewSet.as_view(
        {'get': 'retrieve_service_category', 'patch': 'update_service_category', 'delete': 'delete_service_category'})),

    path('services/', views.ServicesViewSet.as_view({'post': 'create_service', 'get': 'list_services'})),
    path('services/<int:pk>/', views.ServicesViewSet.as_view(
        {'get': 'retrieve_service', 'patch': 'update_service', 'delete': 'delete_service'})),

    path('additional/link/', views.AdditionalLinksViewSet.as_view(
        {'post': 'create_additional_links', 'get': 'list_additional_links'})),
    path('additional/link/<int:pk>/', views.AdditionalLinksViewSet.as_view(
        {'get': 'retrieve_additional_link', 'patch': 'update_additional_link', 'delete': 'delete_additional_link'})),

    path('partners/', views.PartnersViewSet.as_view({'post': 'create_partner', 'get': 'list_partners'})),
    path('partners/<int:pk>/', views.PartnersViewSet.as_view(
        {'get': 'retrieve_partner', 'patch': 'update_partner', 'delete': 'delete_partner'})),

    path('document/category/', views.DocumentCategoryViewSet.as_view(
        {'post': 'create_document_category', 'get': 'list_document_category'})),
    path('document/category/<int:pk>/', views.DocumentCategoryViewSet.as_view(
        {'get': 'retrieve_document_category', 'patch': 'update_document_category', 'delete': 'delete_document_category'}
    )),

    path('document/type/', views.DocumentTypeViewSet.as_view(
        {'post': 'create_document_type', 'get': 'list_document_type'})),
    path('document/type/<int:pk>/', views.DocumentTypeViewSet.as_view(
        {'get': 'retrieve_document_type', 'patch': 'update_document_type', 'delete': 'delete_document_type'})),

    path('document/order/', views.DocumentOrderViewSet.as_view(
        {'post': 'create_document_order', 'get': 'list_document_order'})),
    path('document/order/<int:pk>/', views.DocumentOrderViewSet.as_view(
        {'get': 'retrieve_document_order', 'patch': 'update_document_order', 'delete': 'delete_document_order'})),

    path('document/ready/', views.ReadyDocumentsViewSet.as_view(
        {'post': 'create_ready_document', 'get': 'list_ready_document'})),
    path('document/ready/<int:pk>/', views.ReadyDocumentsViewSet.as_view(
        {'get': 'retrieve_ready_document', 'patch': 'update_ready_document', 'delete': 'delete_ready_document'})),

    path('meeting/order/', views.MeetingOrderViewSet.as_view(
        {'post': 'create_meeting_order', 'get': 'list_meeting_order'})),
    path('meeting/order/<int:pk>/', views.MeetingOrderViewSet.as_view(
        {'get': 'retrieve_meeting_order', 'patch': 'update_meeting_order', 'delete': 'delete_meeting_order'})),

    path('contacts/', views.ContactsViewSet.as_view({'post': 'create_contacts', 'get': 'list_contacts'})),
    path('contacts/<int:pk>/', views.ContactsViewSet.as_view(
        {'get': 'retrieve_contacts', 'patch': 'update_contacts', 'delete': 'delete_contacts'})),
]
