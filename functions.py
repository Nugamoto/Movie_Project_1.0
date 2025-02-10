import statistics
from random import choice

menu = ["Exit",
        "List movies",
        "Add movie",
        "Delete movie",
        "Update movie",
        "Stats",
        "Random movie",
        "Search movie",
        "Movies sorted by rating"
        ]

movies = {
    "Title": {
        "The Shawshank Redemption": {"Rating": 9.5, "Year of release": 1994},
        "Pulp Fiction": {"Rating": 8.8, "Year of release": 1994},
        "The Room": {"Rating": 3.6, "Year of release": 2003},
        "The Godfather": {"Rating": 9.2, "Year of release": 1972},
        "The Godfather: Part II": {"Rating": 9.0, "Year of release": 1974},
        "The Dark Knight": {"Rating": 9.5, "Year of release": 2008},
        "12 Angry Men": {"Rating": 8.9, "Year of release": 1957},
        "Everything Everywhere All At Once": {"Rating": 4, "Year of release": 2022},
        "Forrest Gump": {"Rating": 6, "Year of release": 1994},
        "Star Wars: Episode V": {"Rating": 5, "Year of release": 1980}
    }
}


def print_title(title: str):
    """
    Prints a formatted title.

    Args:
        title (str): The title to be printed.
    """
    print(f"\n********** {title} **********")


def print_menu(menu: list):
    """
    Prints a menu with numbered options.

    Args:
        menu (list): A list of menu options.
    """
    print("\nMenu:")
    for number, element in enumerate(menu):
        print(f"{number}. {element}")
    print("\n")


def ask_for_number():
    """
    Prompts the user to enter a number between 0 and 8.

    Returns:
        int: The number entered by the user if valid.
    """
    while True:
        try:
            number = int(input("Enter choice (0-8): "))
            if 0 <= number <= 8:
                return number
            print("The choice must be between 0 and 8. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number!")


def press_enter_to_continue() -> bool:
    """
    Prompts the user to press Enter to continue.

    Returns:
        bool: Always returns False.
    """
    input("\nPress enter to continue: ")
    return False


def show_all_movies(movies: dict):
    """
    Displays all movies and their ratings.

    Args:
        movies (dict[str, dict]): A dictionary containing movies as keys and their ratings as values.
    """
    print(f"\n----- Total of {len(movies["Title"])} movies -----")
    for title, data in movies["Title"].items():
        print(f"'{title}'\n\tRating: {float(data["Rating"])} | Year: {data["Year of release"]} ")


def add_movie(movies: dict):
    """
    Adds a new movie with its rating and year of release to the collection.

    Args:
        movies (dict[str, dict]): A dictionary containing movies as keys and their details as values.

    Returns:
        dict: The updated dictionary with the new movie added.
    """
    movie = input("Enter new movie name: ")
    if movie not in movies["Title"]:
        while True:
            try:
                rating = float(input("Enter new movie rating (0-10): "))
                if 0 <= rating <= 10:
                    break
                print(f"Rating {rating} is invalid. Please try again!")
            except ValueError:
                print("Invalid input. Please enter a valid number!")

        while True:
            try:
                year = int(input("Enter year of release: "))
                if 1000 <= year <= 9999:
                    break
                print("Invalid year. Please enter a 4-digit year!")
            except ValueError:
                print("Invalid input. Please enter a valid 4-digit year!")

        print(
            f"\nMovie '{movie}' (Rating: {rating}, Year: {year}) successfully added"
        )
        movies["Title"][movie] = {"Rating": rating, "Year of release": year}
    else:
        print(f"\n'{movie}' already exists.")

    return movies


def delete_movie(movies: dict):
    """
    Deletes a movie from the collection.

    Args:
        movies (dict[str, dict]): A dictionary containing movies as keys and their ratings as values.

    Returns:
        dict: The updated dictionary with the movie removed.
    """
    movie = input("Enter movie name to delete: ")
    if movie in movies["Title"]:
        print(f"\nMovie '{movie}' successfully deleted")
        del movies["Title"][movie]
    else:
        print(f"\nMovie '{movie}' doesn't exist!")
    return movies


def update_movie(movies: dict):
    """
    Updates the rating of an existing movie.

    Args:
        movies (dict[str, dict]): A dictionary containing movies as keys and their details as values.

    Returns:
        dict: The updated dictionary with the new rating.
    """
    movie = input("Enter movie name to update: ")
    if movie not in movies["Title"]:
        print(f"\nMovie '{movie}' doesn't exist!")
    else:
        while True:
            try:
                new_rating = float(input("Enter new movie rating (0-10): "))
                if 0 <= new_rating <= 10:
                    break
                print(f"Rating {new_rating} is invalid. Please try again!")
            except ValueError:
                print("Invalid input. Please enter a valid number!")

        print(f"\nMovie '{movie}' successfully updated")
        movies["Title"][movie]["Rating"] = float(round(new_rating, 1))

    return movies


def get_average_rating(movies: dict):
    """
    Calculates the average rating of all movies.

    Args:
        movies (dict): A dictionary where the key "Title" maps to another dictionary
                       containing movie names as keys and their details (including "Rating") as values.

    Returns:
        float or None: The average rating rounded to one decimal place, or None if no ratings exist.
    """
    ratings = [details["Rating"] for details in movies["Title"].values()]
    return round(sum(ratings) / len(ratings), 1) if ratings else None


def get_median_rating(movies: dict):
    """
    Calculates the median rating of all movies.

    Args:
        movies (dict): A dictionary where the key "Title" maps to another dictionary
                       containing movie names as keys and their details (including "Rating") as values.

    Returns:
        float or None: The median rating rounded to one decimal place, or None if no ratings exist.
    """
    ratings = sorted([details["Rating"] for details in movies["Title"].values()])
    return round(statistics.median(ratings), 1) if ratings else None


def get_best_rated_movie(movies: dict):
    """
    Finds the highest-rated movie.

    Args:
        movies (dict): A dictionary where the key "Title" maps to another dictionary
                       containing movie names as keys and their details (including "Rating") as values.

    Returns:
        tuple or None: A tuple containing the name and rating of the highest-rated movie,
                       or None if no movies exist.
    """
    best_rated_movie = None
    best_rating = 0.0

    for movie, data in movies["Title"].items():
        if data["Rating"] > best_rating:
            best_rating = data["Rating"]
            best_rated_movie = movie

    return (best_rated_movie, best_rating) if best_rated_movie else None


def get_worst_rated_movie(movies: dict):
    """
    Finds the lowest-rated movie.

    Args:
        movies (dict): A dictionary where the key "Title" maps to another dictionary
                       containing movie names as keys and their details (including "Rating") as values.

    Returns:
        tuple or None: A tuple containing the name and rating of the lowest-rated movie,
                       or None if no movies exist.
    """
    worst_rated_movie = None
    worst_rating = 10.0

    for movie, data in movies["Title"].items():
        if data["Rating"] < worst_rating:
            worst_rating = data["Rating"]
            worst_rated_movie = movie

    return (worst_rated_movie, worst_rating) if worst_rated_movie else None


def get_random_movie(movies: dict):
    """
    Selects a random movie from the collection.

    Args:
        movies (dict[str, dict]): A dictionary containing movies as keys and their ratings as values.

    Returns:
        tuple: The name and data of the randomly selected movie.
    """
    random_movie_name = (choice(list(movies["Title"])))
    random_movie_data = movies["Title"][random_movie_name]
    return random_movie_name, random_movie_data


def find_movies(movies: dict):
    """
    Finds movies that contain a specific substring in their name.

    Args:
        movies (dict[str, dict]): A dictionary containing movies as keys and their ratings as values.

    Returns:
        dict: A dictionary of movies that match the search criteria.
    """
    part_of_movie_name = input("Enter part of movie name: ")
    found_items = {}
    for title, data in movies["Title"].items():
        if part_of_movie_name.lower() in title.lower():
            found_items[title] = data
    return found_items


def sort_movies_from_highest_to_lowest(movies: dict):
    """
    Sorts movies by their ratings in descending order.

    Args:
        movies (dict): A dictionary containing movies as keys and their details as values.

    Returns:
        dict: A dictionary of movies sorted by ratings from highest to lowest.
    """
    sorted_movies = dict(sorted(movies["Title"].items(), key=lambda item: item[1]["Rating"], reverse=True))
    return {"Title": sorted_movies}
