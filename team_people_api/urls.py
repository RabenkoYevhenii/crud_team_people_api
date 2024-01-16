from django.urls import path, include
from rest_framework import routers

from team_people_api import views

router = routers.DefaultRouter()

router.register("people", views.PeopleViewSet)
router.register("teams", views.TeamViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "team_people_api"
