from django.contrib import admin
from .models import Director, Genre, Movie, Review


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director', 'get_genres')
    search_fields = ('name',)
    filter_horizontal = ('genres',)

    @admin.display(description='GENRES')
    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('genres')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'rating', 'status', 'comment', 'created_at')
    list_filter = ('status', 'rating')
    search_fields = ('movie__name', 'comment')
    list_editable = ('status', 'rating')
    actions = ['mark_as_completed']

    @admin.action(description='Позначити як переглянуті')
    def mark_as_completed(self, request, queryset):
        updated = queryset.update(status=Review.StatusChoices.COMPLETED)
        self.message_user(request, f'Оновлено {updated} записів.')