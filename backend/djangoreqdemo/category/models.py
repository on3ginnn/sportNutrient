from django.db import models
import django.core
import django.db

import core.models


class Category(
    core.models.CategoryProductAbstractModel,
):
    slug = django.db.models.SlugField(
        max_length=200,
        verbose_name="слаг",
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
