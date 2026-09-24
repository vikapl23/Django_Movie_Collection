import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from movies.models import Movie, Review
from django.db.models import Count


print("--- 1. All records of the main model ---")
all_reviews = Review.objects.all()
print('1:', list(all_reviews))


print("\n--- 2. Filter by a numeric field (rating >= 8) ---")
high_rated = Review.objects.filter(rating__gte=8)
print('2:', list(high_rated))


print("\n--- 3. Filter by a related model (movies in the 'Drama' genre) ---")
drama_reviews = Review.objects.filter(movie__genres__name='Drama').distinct()
print('3:', list(drama_reviews))


print("\n--- 4. Filter by a choices field (status 'Completed') ---")
completed_reviews = Review.objects.filter(status=Review.StatusChoices.COMPLETED)
print('4:', list(completed_reviews))


print("\n--- 5. Ordering + slicing (top 3 by rating) ---")
top_3_reviews = Review.objects.order_by('-rating')[:3]
print('5:', list(top_3_reviews))


print("\n--- 6. Counting with annotate (number of genres per movie) ---")
movies_with_genre_count = Movie.objects.annotate(genre_count=Count('genres'))
for i, movie in enumerate(movies_with_genre_count, start=1):
    print(f"{i}: Movie '{movie.name}' has {movie.genre_count} genre(s)")


print("\n--- 7. Any query + its SQL via .query ---")
complex_query = Review.objects.filter(
    rating__gt=7,
    movie__genres__name='Science Fiction'
).distinct()

print('7 Result:', list(complex_query))
print('7 SQL Query:')
print(complex_query.query)
