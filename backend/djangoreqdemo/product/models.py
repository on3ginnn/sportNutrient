from django.db import models
import django.core
import django.db.models

import core.models
import category.models
import product.models


class ItemManager(django.db.models.Manager):
    def item_all(self):

        item_category = product.models.Item.category.field.name
        category_name = category.models.Category.title.field.name

        return (
            self.get_queryset()
            .select_related(
                "category",
            )
            .only("title", "category__title", "description")
            .order_by(
                "-created",
                f"{item_category}__{category_name}",
            )
        )


class Item(
    core.models.CategoryProductAbstractModel,
):
    objects = ItemManager()

    category = django.db.models.ForeignKey(
        category.models.Category,
        verbose_name="Категория",
        on_delete=django.db.models.CASCADE,
        related_name="product_items",
        related_query_name="item",
        default=None,
        help_text="Выберите категорию",
    )
    description = django.db.models.TextField(
        verbose_name="текст",
        help_text='описание товара"',
    )

    created = django.db.models.DateTimeField(
        "дата создания",
        auto_now_add=True,
        null=True,
    )

    updated = django.db.models.DateTimeField(
        "дата изменения",
        auto_now=True,
        null=True,
    )

    class Meta:
        ordering = ("-created",)
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.title
