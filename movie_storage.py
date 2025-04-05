import json


def get_movies():
    try:
        with open("data.json", "r") as content:
            return json.loads(content.read())
    except (FileNotFoundError, json.JSONDecodeError):
        return {"Title": {}}


def save_movies(movies):
    with open("data.json", "w") as content:
        content.write(json.dumps(movies))


def add_movie(title, rating, year):
    movies = get_movies()

    movies["Title"][title] = {"Rating": float(round(rating, 1)), "Year of release": year}

    print(f"\nMovie '{title}' (Rating: {rating}, Year: {year}) successfully added")

    save_movies(movies)


def delete_movie(title):
    movies = get_movies()

    del movies["Title"][title]

    print(f"\nMovie '{title}' successfully deleted")

    save_movies(movies)


def update_movie(title, rating):
    movies = get_movies()

    movies["Title"][title]["Rating"] = float(round(rating, 1))

    print(f"\nMovie '{title}' successfully updated")

    save_movies(movies)
