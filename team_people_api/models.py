from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField("People", related_name="teams", blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class People(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        ordering = ["first_name", "last_name"]
        verbose_name_plural = "people"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
