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
        "Movies sorted by rating",
        "Movies sorted by year"
        ]


def print_title(title: str):
    """
    Prints a formatted title.

    Args:
        title (str): The title to be printed.
    """
    print(f"\n********** {title} **********")


def print_menu(menu):
    """
    Prints a menu with numbered options.

    Args:
        menu (list): A list of menu options.
    """
    print("\nMenu:")
    for number, element in enumerate(menu):
        print(f"{number}. {element}")
    print("\n")


def ask_for_number(menu):
    """
    Prompts the user to enter a number between 0 and len(menu).

    Returns:
        int: The number entered by the user if valid.
    """
    final_digit = len(menu) - 1
    while True:
        try:
            number = int(input(f"Enter choice (0-{final_digit}): "))
            if 0 <= number <= final_digit:
                return number
            print(f"The choice must be between 0 and {final_digit}. Please try again.")
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


def show_movies(movies):
    """
    Displays all movies, their ratings and years of release.

    Args:
        movies (dict[str, dict]): A dictionary containing movies as keys and their ratings as values.
    """
    print(f"\n----- Total of {len(movies["Title"])} movies -----")
    for title, data in movies["Title"].items():
        print(f"'{title}'\n\tRating: {float(data["Rating"])} | Year: {data["Year of release"]} ")


def add_movie(movies):
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


def delete_movie(movies):
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


def update_movie(movies):
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


def get_average_rating(movies):
    ratings = [details["Rating"] for details in movies["Title"].values()]
    return round(sum(ratings) / len(ratings), 1) if ratings else None


def get_median_rating(movies):
    ratings = sorted([details["Rating"] for details in movies["Title"].values()])
    return round(statistics.median(ratings), 1) if ratings else None


def get_best_rated_movie(movies):
    best_rated_movie = None
    best_rating = 0.0

    for movie, data in movies["Title"].items():
        if data["Rating"] > best_rating:
            best_rating = data["Rating"]
            best_rated_movie = movie

    return (best_rated_movie, best_rating) if best_rated_movie else None


def get_worst_rated_movie(movies):
    worst_rated_movie = None
    worst_rating = 10.0

    for movie, data in movies["Title"].items():
        if data["Rating"] < worst_rating:
            worst_rating = data["Rating"]
            worst_rated_movie = movie

    return (worst_rated_movie, worst_rating) if worst_rated_movie else None


def get_random_movie(movies):
    random_movie_name = (choice(list(movies["Title"])))
    random_movie_data = movies["Title"][random_movie_name]
    return random_movie_name, random_movie_data


def find_movies(movies):
    part_of_movie_name = input("Enter part of movie name: ")
    found_items = {"Title": {}}
    for title, data in movies["Title"].items():
        if part_of_movie_name.lower() in title.lower():
            found_items["Title"][title] = data
    return found_items


def sort_movies_by_rating(movies, order):
    sorted_movies = dict(sorted(movies["Title"].items(), key=lambda item: item[1]["Rating"], reverse=order))
    return {"Title": sorted_movies}


def get_title_from_user():
    return input("Enter movie name: ")


def get_valid_year_from_user():
    while True:
        try:
            year = int(input("Enter year of release: "))
            if 1000 <= year <= 9999:
                break
            print("Invalid year. Please enter a 4-digit year!")
        except ValueError:
            print("Invalid input. Please enter a valid 4-digit year!")
    return year


def get_valid_rating_from_user():
    while True:
        try:
            rating = round(float(input("Enter new movie rating (0-10): ")), 1)
            if 0 <= rating <= 10:
                break
            print(f"Rating {rating} is invalid. Please try again!")
        except ValueError:
            print("Invalid input. Please enter a valid number!")
    return rating


def sort_movies_by_year(movies, order):
    sorted_movies = dict(sorted(movies["Title"].items(), key=lambda item: item[1]["Year of release"], reverse=order))
    return {"Title": sorted_movies}


def ask_user_for_sequence():
    while True:
        sequence = input(f"\nEnter '1' for ascending sequence.\n"
                         f"Enter '2' for descending sequence.\n")
        if sequence == "1":
            return False
        elif sequence == "2":
            return True
        else:
            print(f"Bad input! Please enter '1' or '2'.")


def display_movie_stats(average, median, best, worst):
    print(f"\n"
          f"----- Stats -----"
          f"\n"
          f"Average rating: {average}\n"
          f"Median rating : {median}\n"
          f"Best movie    : '{best[0]}', Rating: {best[1]}\n"
          f"Worst movie   : '{worst[0]}', Rating: {worst[1]}"
          )


def display_found_movies(found_movies):
    print("\n")
    if found_movies["Title"] == {}:
        print(f"No movie found.")
    else:
        show_movies(found_movies)


def display_random_movie(random_movie):
    print(f"\n"
          f"Your movie for tonight:\n"
          f"'{random_movie[0]}'\nIt's rated {float(random_movie[1]["Rating"])} "
          f"and released {random_movie[1]["Year of release"]}.")
