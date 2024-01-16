from django import forms

from team_people_api.models import People, Team


class TeamForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=People.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )

    class Meta:
        model = Team
        fields = "__all__"
