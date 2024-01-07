from rest_framework.routers import DefaultRouter
from django.urls import include, path
from rest_framework import routers

from apps.multichoice_corrector.views import correct

router = DefaultRouter()

urlpatterns = [
    path('correct/', correct),
]

urlpatterns += router.urls
