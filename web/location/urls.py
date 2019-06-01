from django.urls import path
from rest_framework.routers import DefaultRouter

from location.views import CityViewSet, CountyViewSet, ProvinceViewSet ,SearchView

router = DefaultRouter()
router.register("cities", CityViewSet, base_name="cities")
router.register("provinces", ProvinceViewSet, base_name="provinces")
router.register("counties", CountyViewSet, base_name="counties")
urlpatterns = router.urls

urlpatterns.append(
    path('search/', SearchView.as_view()),
)
