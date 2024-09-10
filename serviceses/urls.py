from django.urls import path
from .views import DocumentCategoryViewSet, DocumentOrderViewSet, ContactsViewSet

urlpatterns = [
    path('category/', DocumentCategoryViewSet.as_view({'get': 'list'}), name='category'),
    path('create/document/', DocumentOrderViewSet.as_view({'post': 'create'}), name='create'),
    path('create/meeting/', DocumentOrderViewSet.as_view({'post': 'create_meeting'}), name='create_meeting'),
    path('create/contacts/', ContactsViewSet.as_view({'post': 'create'}), name='create_contacts'),
]
