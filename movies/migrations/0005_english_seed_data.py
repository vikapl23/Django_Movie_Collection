from django.db import migrations

# Old Ukrainian names -> English names (for databases filled before the site was translated)
GENRE_RENAMES = {
    'Драма': 'Drama',
    'Трилер': 'Thriller',
    'Комедія': 'Comedy',
    'Фантастика': 'Science Fiction',
    'Наукова фантастика': 'Science Fiction',
}

MOVIE_RENAMES = {
    '1+1': 'The Intouchables',
    'Дедпул': 'Deadpool',
    'Джокер': 'Joker',
    'Дюна': 'Dune',
    'Той, хто біжить по лезу 2049': 'Blade Runner 2049',
    'Аватар': 'Avatar',
    'Мисливці за привидами': 'Ghostbusters',
    'Зелена книга': 'Green Book',
    'Зоряні війни: Нова надія': 'Star Wars: A New Hope',
}

COMMENT_RENAMES = {
    'Дедпул — дуже веселий і динамічний фільм із чорним гумором, яскравими персонажами та великою '
    'кількістю екшену. Головний герой постійно жартує і ламає типові правила супергеройських фільмів.':
        'Deadpool is a very funny, fast-paced movie with dark humor, vivid characters and plenty of action. '
        'The main character constantly cracks jokes and breaks the usual rules of superhero movies.',
}

# name: (director, genres, description, [(rating, status, comment), ...])
MOVIES = {
    'The Intouchables': (
        'Olivier Nakache', ['Drama', 'Comedy'],
        'A wealthy aristocrat left paralysed after an accident hires a young man from the projects '
        'as his caregiver, and the two form an unlikely friendship.',
        [],
    ),
    'Deadpool': (
        'Tim Miller', ['Action', 'Comedy'],
        'A former special forces operative turned mercenary gains healing powers after a rogue '
        'experiment and hunts down the man who nearly destroyed his life.',
        [],
    ),
    'Joker': (
        'Todd Phillips', ['Drama', 'Thriller', 'Crime'],
        'A failed comedian in Gotham City slowly descends into madness and becomes the infamous Joker.',
        [],
    ),
    'Dune': (
        'Denis Villeneuve', ['Science Fiction', 'Adventure'],
        'Paul Atreides travels to the dangerous desert planet Arrakis to protect his family and the '
        'future of his people.',
        [],
    ),
    'Blade Runner 2049': (
        'Denis Villeneuve', ['Science Fiction', 'Thriller', 'Drama'],
        'A young blade runner uncovers a long-buried secret that leads him to track down former '
        'blade runner Rick Deckard.',
        [],
    ),
    'Avatar': (
        'James Cameron', ['Science Fiction', 'Adventure'],
        'A paraplegic Marine on the alien moon Pandora is torn between following orders and '
        'protecting the world he now feels is his home.',
        [],
    ),
    'Ghostbusters': (
        'Ivan Reitman', ['Comedy', 'Science Fiction'],
        'Three parapsychologists start a ghost-catching business in New York City just as the '
        'city faces a supernatural invasion.',
        [],
    ),
    'Green Book': (
        'Peter Farrelly', ['Drama', 'Comedy'],
        'A working-class Italian-American bouncer becomes the driver of a world-class African-American '
        'pianist on a concert tour through the 1960s American South.',
        [],
    ),
    'Star Wars: A New Hope': (
        'George Lucas', ['Science Fiction', 'Adventure', 'Action'],
        'Luke Skywalker joins a Jedi Knight, a cocky pilot and two droids to rescue Princess Leia '
        'and save the galaxy from the Empire.',
        [],
    ),
    'Inception': (
        'Christopher Nolan', ['Science Fiction', 'Action', 'Thriller'],
        'A thief who steals corporate secrets through dream-sharing technology is given the task '
        'of planting an idea into the mind of a CEO.',
        [(10, 'completed', 'Mind-bending plot and an incredible soundtrack. Worth rewatching.')],
    ),
    'Interstellar': (
        'Christopher Nolan', ['Science Fiction', 'Drama', 'Adventure'],
        'A team of explorers travels through a wormhole in space to find a new home for humanity.',
        [(9, 'completed', 'Beautiful and emotional. The docking scene is unforgettable.')],
    ),
    'The Dark Knight': (
        'Christopher Nolan', ['Action', 'Crime', 'Drama'],
        'Batman faces the Joker, a criminal mastermind who wants to plunge Gotham City into anarchy.',
        [(10, 'completed', "Heath Ledger's Joker is one of the best villains ever.")],
    ),
    'The Shawshank Redemption': (
        'Frank Darabont', ['Drama', 'Crime'],
        'A banker sentenced to life in Shawshank prison finds hope and friendship over two decades.',
        [(10, 'completed', 'A powerful story about hope and patience.')],
    ),
    'The Godfather': (
        'Francis Ford Coppola', ['Crime', 'Drama'],
        'The aging patriarch of a crime dynasty transfers control of his empire to his reluctant son.',
        [(9, 'completed', '')],
    ),
    'Pulp Fiction': (
        'Quentin Tarantino', ['Crime', 'Thriller'],
        'The lives of two mob hitmen, a boxer, a gangster and his wife intertwine in four tales of '
        'violence and redemption.',
        [(8, 'completed', 'Great dialogue and a clever non-linear structure.')],
    ),
    'Parasite': (
        'Bong Joon-ho', ['Thriller', 'Drama', 'Comedy'],
        'A poor family schemes to become employed by a wealthy family by posing as unrelated, '
        'highly qualified individuals.',
        [(9, 'completed', 'Funny, tense and shocking at the same time.')],
    ),
    'Spirited Away': (
        'Hayao Miyazaki', ['Animation', 'Fantasy', 'Adventure'],
        'A ten-year-old girl wanders into a world ruled by gods and spirits, where her parents are '
        'turned into pigs.',
        [(9, 'completed', 'Pure magic from start to finish.')],
    ),
    'The Lord of the Rings: The Fellowship of the Ring': (
        'Peter Jackson', ['Fantasy', 'Adventure'],
        'A humble hobbit and eight companions set out on a journey to destroy the powerful One Ring.',
        [(9, 'completed', '')],
    ),
    'The Matrix': (
        'Lana Wachowski', ['Science Fiction', 'Action'],
        'A computer hacker learns that the world he lives in is a simulation and joins a rebellion '
        'against its controllers.',
        [(8, 'completed', 'Still looks amazing today.')],
    ),
    'Get Out': (
        'Jordan Peele', ['Horror', 'Thriller'],
        "A young man visits his girlfriend's family estate, where his uneasiness about their "
        'reception turns into something much darker.',
        [(8, 'completed', '')],
    ),
    'La La Land': (
        'Damien Chazelle', ['Romance', 'Drama', 'Comedy'],
        'An aspiring actress and a jazz pianist fall in love while pursuing their dreams in Los Angeles.',
        [(7, 'completed', 'Lovely music, bittersweet ending.')],
    ),
    'Whiplash': (
        'Damien Chazelle', ['Drama'],
        'A promising young drummer enrolls at a cut-throat music conservatory where his teacher '
        'will stop at nothing to realise his potential.',
        [(9, 'completed', 'Intense from the first to the last minute.')],
    ),
    'Toy Story': (
        'John Lasseter', ['Animation', 'Comedy', 'Adventure'],
        "A cowboy doll feels threatened when a new spaceman action figure becomes his owner's favourite toy.",
        [(8, 'completed', '')],
    ),
    'Oppenheimer': (
        'Christopher Nolan', ['Drama', 'Thriller'],
        'The story of J. Robert Oppenheimer and his role in the development of the atomic bomb.',
        [(8, 'watching', '')],
    ),
    'Gladiator': (
        'Ridley Scott', ['Action', 'Drama', 'Adventure'],
        'A former Roman general sets out to take revenge on the corrupt emperor who murdered his '
        'family and sent him into slavery.',
        [],
    ),
    'Everything Everywhere All at Once': (
        'Daniel Kwan', ['Science Fiction', 'Comedy', 'Action'],
        'A laundromat owner discovers she must connect with parallel-universe versions of herself '
        'to prevent a powerful being from destroying the multiverse.',
        [(6, 'planned', '')],
    ),
    'The Silence of the Lambs': (
        'Jonathan Demme', ['Thriller', 'Crime', 'Horror'],
        'A young FBI cadet seeks the help of an imprisoned cannibal killer to catch another serial killer.',
        [],
    ),
    'Coco': (
        'Lee Unkrich', ['Animation', 'Fantasy', 'Comedy'],
        'Aspiring musician Miguel enters the Land of the Dead to find his great-great-grandfather, '
        'a legendary singer.',
        [(9, 'completed', 'Made me cry. Beautiful animation.')],
    ),
}


def seed(apps, schema_editor):
    Genre = apps.get_model('movies', 'Genre')
    Director = apps.get_model('movies', 'Director')
    Movie = apps.get_model('movies', 'Movie')
    Review = apps.get_model('movies', 'Review')

    for old, new in GENRE_RENAMES.items():
        for genre in Genre.objects.filter(name=old):
            existing = Genre.objects.filter(name=new).exclude(pk=genre.pk).first()
            if existing:
                for movie in genre.movies.all():
                    movie.genres.add(existing)
                genre.delete()
            else:
                genre.name = new
                genre.save()

    for old, new in MOVIE_RENAMES.items():
        Movie.objects.filter(name=old).update(name=new)

    for old, new in COMMENT_RENAMES.items():
        Review.objects.filter(comment=old).update(comment=new)

    for name, (director_name, genre_names, description, reviews) in MOVIES.items():
        director, _ = Director.objects.get_or_create(name=director_name)
        genres = [Genre.objects.get_or_create(name=g)[0] for g in genre_names]

        existing = Movie.objects.filter(name=name)
        if existing.exists():
            # fill in missing details of movies that were added earlier
            for movie in existing:
                if movie.director_id is None:
                    movie.director = director
                if not movie.description:
                    movie.description = description
                movie.save()
                if not movie.genres.exists():
                    movie.genres.set(genres)
            continue

        movie = Movie.objects.create(name=name, director=director, description=description)
        movie.genres.set(genres)
        for rating, status, comment in reviews:
            Review.objects.create(movie=movie, rating=rating, status=status, comment=comment)


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_english_status_labels'),
    ]

    operations = [
        migrations.RunPython(seed, migrations.RunPython.noop),
    ]
