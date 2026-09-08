from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name='movies')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Review(models.Model):
    class StatusChoices(models.TextChoices):
        PLANNED = 'planned', 'В планах'
        WATCHING = 'watching', 'Дивлюсь'
        COMPLETED = 'completed', 'Переглянуто'
        ABANDONED = 'abandoned', 'Покинуто'

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PLANNED,
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.movie.name} ({self.get_status_display()}) - {self.rating}/10"

    @property
    def is_completed(self):
        return self.status == self.StatusChoices.COMPLETED