# states/urls.py
from django.urls import path
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from .views import PersonList, PersonDetail

urlpatterns = [
    path('people/', PersonList.as_view(), name='person-list'),
    path('people/<int:pk>/', PersonDetail.as_view(), name='person-detail'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
