from django.db import models
import django.db.models


class CategoryProductAbstractModel(django.db.models.Model):
    title = django.db.models.CharField(
        max_length=150,
        verbose_name="название",
        help_text="max 150 символов",
        unique=True,
    )

    class Meta:
        abstract = True