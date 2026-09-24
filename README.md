# 🎬 My Movie Diary — Django Movie Collection Tracker

A Django web app for keeping a personal movie collection: add movies, tag them with genres and directors, and track reviews with ratings and watch statuses.

## Features

- Browse all movies with pagination (5 per page)
- Filter movies by review rating: buttons 1–10 show only movies that have a review with exactly that rating
- A **Top rated** page listing movies that have at least one review rated 8+
- Movie detail pages with the director, genres, description, reviews and other movies by the same director
- Genre list with the number of movies in each genre
- User accounts: sign up (with automatic login), log in, log out, change password
- Logged-in users can add movies and see them on the **My movies** page
- Only a movie's owner can edit or delete it
- Flash messages after creating and updating a movie
- Custom admin panel with search, filters, inline editing and a bulk "Mark as completed" action
- A standalone `queries.py` script that demonstrates Django ORM queries

## Tech Stack

- Python 3.12+
- Django 6.1
- SQLite
- [django-environ](https://django-environ.readthedocs.io/) for settings from a `.env` file
- [WhiteNoise](https://whitenoise.readthedocs.io/) for serving static files
- Gunicorn (Linux/macOS) or Waitress (Windows) as the production WSGI server
- [uv](https://docs.astral.sh/uv/) as the package manager

## Project Structure

```
Django_Movie_Collection/
├── config/                 # Project settings, root URLs, WSGI/ASGI
├── movies/                 # Main app
│   ├── models.py           # Genre, Director, Movie, Review
│   ├── views.py            # Function-based views and class-based views
│   ├── admin.py            # Admin configuration
│   ├── migrations/
│   └── templates/
│       ├── movies/         # base, home, movie list/detail/form/delete, genres
│       └── registration/   # login, signup, password change
├── screenshots/            # Admin screenshots used in this README
├── queries.py              # ORM query demo script
├── .env.example            # Example environment variables
├── pyproject.toml / uv.lock
└── requirements.txt
```

## Models

| Model | Fields | Relations |
|---|---|---|
| **Genre** | `name` | — |
| **Director** | `name` | — |
| **Movie** | `name`, `description` | `genres` → `Genre` (ManyToMany), `director` → `Director` (ForeignKey, optional, `SET_NULL`), `owner` → `User` (ForeignKey, optional, `CASCADE`) |
| **Review** | `rating` (1–10), `status`, `comment`, `created_at` | `movie` → `Movie` (ForeignKey, `CASCADE`) |

`Review.status` is one of: **Planned**, **Watching**, **Completed**, **Abandoned**.

## Pages & Routes

| Route | View | Access | Description |
|---|---|---|---|
| `/` | `home` | Everyone | Home page with links to movies and genres |
| `/movies/` | `MovieListView` | Everyone | All movies, paginated |
| `/movies/?rating=<1-10>` | `MovieListView` | Everyone | Movies with a review of exactly that rating |
| `/movies/top-rated/` | `TopRatedMoviesView` | Everyone | Movies with at least one review rated 8+ |
| `/movies/my/` | `MyMoviesView` | Logged in | Movies added by the current user |
| `/movies/new/` | `MovieCreateView` | Logged in | Add a new movie |
| `/movies/<pk>/` | `MovieDetailView` | Everyone | Movie details, reviews, other movies by the director |
| `/movies/<pk>/edit/` | `MovieUpdateView` | Owner only | Edit a movie |
| `/movies/<pk>/delete/` | `MovieDeleteView` | Owner only | Confirm and delete a movie |
| `/genres/` | `genre_list` | Everyone | Genres with movie counts |
| `/accounts/signup/` | `SignUpView` | Everyone | Create an account |
| `/accounts/login/`, `/accounts/logout/`, `/accounts/password_change/` | Django auth views | — | Authentication |
| `/admin/` | Django admin | Staff | Admin panel |

---

## Getting Started

### 1. Install uv

Check whether uv is installed:

```bash
uv --version
```

If it isn't, install it:

* **macOS / Linux:**

  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

* **Windows (PowerShell):**

  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

### 2. Install dependencies

```bash
uv sync
```

This creates a virtual environment in `.venv` and installs all dependencies. Then activate it:

* **Windows:** `.venv\Scripts\activate`
* **macOS / Linux:** `source .venv/bin/activate`

(Alternatively, use `pip install -r requirements.txt` in any virtual environment.)

### 3. Configure environment variables

Copy the example file and edit it:

```bash
cp .env.example .env
```

| Variable | Description | Example |
|---|---|---|
| `SECRET_KEY` | Django secret key (required) | a long random string |
| `DEBUG` | Debug mode (defaults to `False`) | `True` for local development |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts | `127.0.0.1,localhost` |

To generate a secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 4. Set up the database

```bash
python manage.py migrate
python manage.py createsuperuser
```

`migrate` also fills the database with sample data (migration `0005_english_seed_data`): 30 movies with directors, genres, descriptions and reviews.

### 5. Run the development server

```bash
python manage.py runserver
```

- Site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

### 6. Run the ORM query demo (optional)

```bash
python queries.py
```

The script prints the results of several ORM queries: all reviews, filtering by rating, by a related genre and by status, ordering with slicing, `annotate` with `Count`, and the raw SQL of a query via `.query`.

---

## Production

Collect static files (served by WhiteNoise):

```bash
python manage.py collectstatic --noinput
```

Run with a production WSGI server:

* **Linux / macOS:**

  ```bash
  gunicorn config.wsgi:application
  ```

* **Windows:**

  ```bash
  waitress-serve --port=8000 config.wsgi:application
  ```

Make sure `DEBUG=False` and `ALLOWED_HOSTS` contains your domain.

---

## Admin Screenshots

### Genres
![Genres](screenshots/img.png)

### Movies
![Movies](screenshots/img_1.png)

### Reviews
![Reviews](screenshots/img_2.png)
