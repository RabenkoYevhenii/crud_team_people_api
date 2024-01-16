from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from team_people_api.models import People, Team
from team_people_api.serializers import (
    PeopleSerializer,
    TeamSerializer,
    TeamListSerializer,
    TeamDetailSerializer,
)


class Pagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    pagination_class = Pagination


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.prefetch_related("members")
    serializer_class = TeamSerializer
    pagination_class = Pagination

    def get_serializer_class(self):
        if self.action == "list":
            return TeamListSerializer

        if self.action == "retrieve":
            return TeamDetailSerializer

        return TeamSerializer
