# Generated by Django 4.2 on 2024-12-08 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Nutrient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="max 150 символов",
                        max_length=150,
                        unique=True,
                        verbose_name="название",
                    ),
                ),
                (
                    "proteins",
                    models.PositiveIntegerField(
                        default=0, null=True, verbose_name="белки"
                    ),
                ),
                (
                    "fats",
                    models.PositiveIntegerField(
                        default=0, null=True, verbose_name="жиры"
                    ),
                ),
                (
                    "carbohydrates",
                    models.PositiveIntegerField(
                        default=0, null=True, verbose_name="углеводы"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="дата изменения"
                    ),
                ),
                (
                    "publisher",
                    models.ForeignKey(
                        default=None,
                        help_text="Выберите автора",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="publisher",
                        related_query_name="publisher",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
            ],
            options={
                "verbose_name": "питательное вещество",
                "verbose_name_plural": "питательные вещества",
                "ordering": ("-created",),
            },
        ),
    ]
