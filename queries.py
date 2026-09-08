import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from movies.models import Movie, Review
from django.db.models import Count


print("--- 1. Усі записи головної моделі ---")
all_reviews = Review.objects.all()
print('1:', list(all_reviews))


print("\n--- 2. Фільтр за числовим полем (оцінка >= 8) ---")
high_rated = Review.objects.filter(rating__gte=8)
print('2:', list(high_rated))


print("\n--- 3. Фільтр за пов'язаною моделлю (фільми жанру 'Драма') ---")
drama_reviews = Review.objects.filter(movie__genres__name='Драма').distinct()
print('3:', list(drama_reviews))


print("\n--- 4. Фільтр за полем choices (статус 'Переглянуто') ---")
completed_reviews = Review.objects.filter(status=Review.StatusChoices.COMPLETED)
print('4:', list(completed_reviews))


print("\n--- 5. Сортування + обмеження (топ-3 фільми за оцінкою) ---")
top_3_reviews = Review.objects.order_by('-rating')[:3]
print('5:', list(top_3_reviews))


print("\n--- 6. Підрахунок через annotate (скільки жанрів у кожного фільму) ---")
movies_with_genre_count = Movie.objects.annotate(genre_count=Count('genres'))
for i, movie in enumerate(movies_with_genre_count, start=1):
    print(f"{i}: Фільм '{movie.name}' має {movie.genre_count} жанр(ів)")


print("\n--- 7. Будь-який запит + вивід його SQL через .query ---")
complex_query = Review.objects.filter(
    rating__gt=7,
    movie__genres__name='Наукова фантастика'
).distinct()

print('7 Result:', list(complex_query))
print('7 SQL Query:')
print(complex_query.query)
