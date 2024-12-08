import django.core
import django.db.models
import django.contrib.auth


class Nutrient(
    django.db.models.Model,
):
    publisher = django.db.models.ForeignKey(
        django.contrib.auth.get_user_model(),
        verbose_name="Автор",
        on_delete=django.db.models.CASCADE,
        related_name="publisher",
        related_query_name="publisher",
        default=None,
        help_text="Выберите автора",
    )
    
    title = django.db.models.CharField(
        max_length=150,
        verbose_name="название",
        help_text="max 150 символов",
        unique=True,
    )

    proteins = django.db.models.PositiveIntegerField(
        "белки",
        default=0,
        null=True,
    )

    fats = django.db.models.PositiveIntegerField(
        "жиры",
        default=0,
        null=True,
    )

    carbohydrates = django.db.models.PositiveIntegerField(
        "углеводы",
        default=0,
        null=True,
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
        verbose_name = "питательное вещество"
        verbose_name_plural = "питательные вещества"

    def __str__(self):
        return self.title
