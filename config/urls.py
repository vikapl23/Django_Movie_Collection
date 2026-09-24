from django.contrib import admin
from django.urls import path, include
from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),

    path('', views.home, name='home'),

    path('movies/new/', views.MovieCreateView.as_view(), name='movie_create'),
    path('movies/top-rated/', views.TopRatedMoviesView.as_view(), name='movie_top_rated'),
    path('movies/my/', views.MyMoviesView.as_view(), name='my_movies'),
    path('movies/', views.MovieListView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('movies/<int:pk>/edit/', views.MovieUpdateView.as_view(), name='movie_update'),
    path('movies/<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movie_delete'),

    path('genres/', views.genre_list, name='genre_list'),
]