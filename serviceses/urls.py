from django.urls import path
from .views import DocumentOrderViewSet, ContactsViewSet, ComplaintViewSet, EvaluationViewSet

urlpatterns = [
    path('create/document/', DocumentOrderViewSet.as_view({'post': 'create'}), name='create'),
    path('document/page/', DocumentOrderViewSet.as_view({'get': 'get_check_page'}), name='get_check_page'),
    path('create/meeting/', DocumentOrderViewSet.as_view({'post': 'create_meeting'}), name='create_meeting'),
    path('check/document/<str:document_id>/', DocumentOrderViewSet.as_view({'get': 'check_document'}),
         name='check_document'),
    path('create/contacts/', ContactsViewSet.as_view({'post': 'create'}), name='create_contacts'),
    path('complaint/<int:pk>/', ComplaintViewSet.as_view({'post': 'create'}), name='complain'),
    path('evaluation/<int:pk>/', EvaluationViewSet.as_view({'post': 'create', 'get': 'check_evaluation'}),
         name='evaluation'),
]
