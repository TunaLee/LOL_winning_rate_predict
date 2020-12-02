from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView

# DRF
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Apps
from backend.apps.inputdata.api.views import InputDataViewSet, SummonerDataViewSet
from backend.apps.champs.api.views import ChampViewSet
from backend.apps.inputdata.api.views import SummonerView


# Main Section
router = routers.DefaultRouter()
router.register(r'InputData', InputDataViewSet, 'InputDataViewSet')
router.register(r'Champ', ChampViewSet, 'ChampViewSet')
router.register(r'SummonerData',SummonerDataViewSet,'SummonerDataViewSet')

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('api/test/summoner/', SummonerView),
    path("api/", include(router.urls)),
    # path('login/', SignInViewSet.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
