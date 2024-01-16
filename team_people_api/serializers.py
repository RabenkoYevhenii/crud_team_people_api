from rest_framework import serializers

from team_people_api.models import Team, People


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
        )


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            "id",
            "name",
        )


class TeamListSerializer(TeamSerializer):
    members = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="last_name"
    )

    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "members",
        )


class TeamDetailSerializer(TeamSerializer):
    members = PeopleSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "members",
        )
