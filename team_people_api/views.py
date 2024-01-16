from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from team_people_api.forms import TeamForm
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

    def perform_create(self, serializer):
        form = TeamForm(self.request.data)
        if form.is_valid():
            team = form.save()
            serializer.save(members=form.cleaned_data['members'])
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        form = TeamForm(self.request.data, instance=self.get_object())
        if form.is_valid():
            team = form.save()
            serializer.save(members=form.cleaned_data['members'])
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)