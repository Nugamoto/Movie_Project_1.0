import json


def get_movies():
    with open("data.json", "r") as content:
        return json.loads(content.read())


def save_movies(movies):
    with open("data.json", "w") as content:
        content.write(json.dumps(movies))


def add_movie(title, year, rating):
    with open("data.json", "r") as content:
        movies = json.loads(content.read())

    if title not in movies["Title"]:
        while True:
            try:
                if 0 <= rating <= 10:
                    break
                print(f"Rating {rating} is invalid. Please try again!")
            except ValueError:
                print("Invalid input. Please enter a valid number!")

        while True:
            try:
                if 1000 <= year <= 9999:
                    break
                print("Invalid year. Please enter a 4-digit year!")
            except ValueError:
                print("Invalid input. Please enter a valid 4-digit year!")

        print(
            f"\nMovie '{title}' (Rating: {rating}, Year: {year}) successfully added"
        )
        movies["Title"][title] = {"Rating": float(round(rating, 1)), "Year of release": year}
    else:
        print(f"\n'{title}' already exists.")

    with open("data.json", "w") as content:
        content.write(json.dumps(movies))


def delete_movie(title):
    with open("data.json", "r") as content:
        movies = json.loads(content.read())

    if title in movies["Title"]:
        print(f"\nMovie '{title}' successfully deleted")
        del movies["Title"][title]
    else:
        print(f"\nMovie '{title}' doesn't exist!")

    with open("data.json", "w") as content:
        content.write(json.dumps(movies))


def update_movie(title, rating):
    with open("data.json", "r") as content:
        movies = json.loads(content.read())

    if title not in movies["Title"]:
        print(f"\nMovie '{title}' doesn't exist!")
    else:
        while True:
            try:
                if 0 <= rating <= 10:
                    break
                print(f"Rating {rating} is invalid. Please try again!")
            except ValueError:
                print("Invalid input. Please enter a valid number!")

        print(f"\nMovie '{title}' successfully updated")
        movies["Title"][title]["Rating"] = float(round(rating, 1))

    with open("data.json", "w") as content:
        content.write(json.dumps(movies))
