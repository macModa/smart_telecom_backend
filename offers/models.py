from django.db import models


class Offer(models.Model):

    CATEGORY_CHOICES = [
        ('mobile', 'Mobile'),
        ('internet', 'Internet'),
        ('fibre', 'Fibre'),
    ]

    title = models.CharField(max_length=200)

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    data_volume = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    call_minutes = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    speed = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    validity_days = models.IntegerField(
        help_text="Validity in days"
    )

    ussd_code = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.category}"
