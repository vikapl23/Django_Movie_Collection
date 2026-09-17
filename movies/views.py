from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Movie, Genre


def home(request):
    return render(request, 'movies/home.html')


# Старі функції

# def movie_list(request):
#     movies = Movie.objects.all()
#     return render(request, 'movies/movie_list.html', {'movies': movies})


# def movie_detail(request, pk):
#     movie = get_object_or_404(Movie, pk=pk)
#     return render(request, 'movies/movie_detail.html', {'movie': movie})


class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    ordering = ['name']
    paginate_by = 5


class TopRatedMoviesView(ListView):
    """Другий ListView: тільки фільми з хоча б одним відгуком з оцінкою 8+."""
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 5

    def get_queryset(self):
        return Movie.objects.filter(reviews__rating__gte=8).distinct().order_by('name')


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all()
        context['other_movies'] = Movie.objects.filter(
            director=self.object.director
        ).exclude(pk=self.object.pk) if self.object.director else Movie.objects.none()
        return context


class MovieCreateView(CreateView):
    model = Movie
    fields = ['name', 'director', 'genres', 'description']
    template_name = 'movies/movie_form.html'

    def form_valid(self, form):
        messages.success(self.request, 'Фільм успішно додано!')
        return super().form_valid(form)


class MovieUpdateView(UpdateView):
    model = Movie
    fields = ['name', 'director', 'genres', 'description']
    template_name = 'movies/movie_form.html'

    def form_valid(self, form):
        messages.success(self.request, 'Зміни збережено!')
        return super().form_valid(form)


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')


def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'movies/genre_list.html', {'genres': genres})