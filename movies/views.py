from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Movie, Genre


def home(request):
    return render(request, 'movies/home.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('movie_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # log the user in right after sign-up
        return response


class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    ordering = ['name']
    paginate_by = 5

    def get_rating(self):
        """Rating from ?rating=N (1-10), or None if missing or invalid."""
        rating = self.request.GET.get('rating', '')
        if rating.isdigit() and 1 <= int(rating) <= 10:
            return int(rating)
        return None

    def get_queryset(self):
        queryset = super().get_queryset()
        rating = self.get_rating()
        if rating is not None:
            queryset = queryset.filter(reviews__rating=rating).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rating = self.get_rating()
        context['rating_filter'] = True
        context['current_rating'] = rating
        context['ratings'] = range(1, 11)
        context['page_title'] = f'Movies rated {rating}/10' if rating else 'All movies'
        return context


class TopRatedMoviesView(ListView):
    """Only movies with at least one review rated 8 or higher."""
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 5
    extra_context = {'page_title': 'Top rated movies', 'ratings': range(1, 11)}

    def get_queryset(self):
        return Movie.objects.filter(reviews__rating__gte=8).distinct().order_by('name')


class MyMoviesView(LoginRequiredMixin, ListView):
    """Movies added by the current user."""
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 5
    extra_context = {'page_title': 'My movies', 'ratings': range(1, 11)}

    def get_queryset(self):
        return Movie.objects.filter(owner=self.request.user)


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


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['name', 'director', 'genres', 'description']
    template_name = 'movies/movie_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Movie added successfully!')
        return response


class MovieUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Movie
    fields = ['name', 'director', 'genres', 'description']
    template_name = 'movies/movie_form.html'

    def test_func(self):
        return self.get_object().owner == self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Changes saved!')
        return response


class MovieDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')

    def test_func(self):
        return self.get_object().owner == self.request.user


def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'movies/genre_list.html', {'genres': genres})