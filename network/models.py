from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


class Product(models.Model):
    """
    Продукт, производимый или продающийся звеном сети.
    """
    name = models.CharField(max_length=255, verbose_name="Название продукта")
    model = models.CharField(max_length=100, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выхода на рынок")

    def __str__(self):
        return f"{self.name} ({self.model})"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ElectronicsNetwork(models.Model):
    """
    Звено иерархической сети продажи электроники.
    Поддерживает 3 уровня:
      0 — Завод
      1 — Розничная сеть
      2 — Индивидуальный предприниматель
    """
    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(max_length=255, verbose_name="Название")

    # Контакты
    email = models.EmailField(verbose_name="Email")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=255, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")

    # Продукты
    products = models.ManyToManyField(Product, blank=True, verbose_name="Продукты")

    # Поставщик (предыдущий уровень)
    supplier = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subordinates',
        verbose_name="Поставщик"
    )

    # Задолженность перед поставщиком
    debt = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00,
        validators=[MinValueValidator(0)],
        verbose_name="Задолженность перед поставщиком (₽)"
    )

    # Время создания
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    # Уровень иерархии (0, 1, 2)
    level = models.PositiveSmallIntegerField(
        choices=LEVEL_CHOICES,
        verbose_name="Уровень иерархии",
        help_text="Определяется автоматически через поставщика"
    )

    def clean(self):
        """
        Валидация уровня иерархии при сохранении.
        """
        if self.level == 0:
            if self.supplier is not None:
                raise ValidationError("Завод (уровень 0) не может иметь поставщика.")
        else:
            if self.supplier is None:
                raise ValidationError("Розничная сеть и ИП должны иметь поставщика.")
            expected_level = self.supplier.level + 1
            if self.level != expected_level:
                raise ValidationError(f"Уровень должен быть {expected_level}.")

    def save(self, *args, **kwargs):
        if self.supplier:
            self.level = self.supplier.level + 1
        else:
            self.level = 0
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Сеть продажи электроники"