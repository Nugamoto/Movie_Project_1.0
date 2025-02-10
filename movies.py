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
        print(f"{number + 1}. {element}")
    print("\n")


def ask_for_number():
    """
    Prompts the user to enter a number between 1 and 8.

    Returns:
        int: The number entered by the user if valid.
    """
    while True:
        try:
            number = int(input("Enter choice (1-8): "))
            if 1 <= number <= 8:
                return number
            print("The choice must be between 1 and 8. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number!")


def continue_or_quit():
    """
    Prompts the user to either continue or quit the application.

    Returns:
        bool: True if the user chooses to quit, otherwise False.
    """
    user_input = input("\nPress enter to continue or 'Q' to quit: ").lower()
    return user_input == "q"


def show_all_movies(movies: dict):
    """
    Displays all movies and their ratings.

    Args:
        movies (dict): A dictionary containing movies as keys and their ratings as values.
    """
    print(f"\n----- Total of {len(movies)} movies -----")
    for key, value in movies.items():
        print(f"{key}: {value}")


def add_movie(movies: dict):
    """
    Adds a new movie and its rating to the collection.

    Args:
        movies (dict): A dictionary containing movies as keys and their ratings as values.

    Returns:
        dict: The updated dictionary with the new movie added.
    """
    movie = input("Enter new movie name: ")
    if movie not in movies:
        while True:
            try:
                rating = float(input("Enter new movie rating (0-10): "))
                if 0 <= rating <= 10:
                    print(
                        f"\nMovie '{movie}' (Rating: {rating}) successfully added"
                    )
                    movies[movie] = rating
                    return movies
                print(f"Rating {rating} is invalid. Please try again!")
            except ValueError:
                print("Invalid input. Please enter a number!")
    else:
        print(f"\n'{movie}' already exists.")


def delete_movie(movies: dict):
    """
    Deletes a movie from the collection.

    Args:
        movies (dict): A dictionary containing movies as keys and their ratings as values.

    Returns:
        dict: The updated dictionary with the movie removed.
    """
    movie = input("Enter movie name to delete: ")
    if movie in movies:
        print(f"\nMovie '{movie}' successfully deleted")
        del movies[movie]
    else:
        print(f"\nMovie '{movie}' doesn't exist!")
    return movies


def update_movie(movies: dict):
    """
    Updates the rating of an existing movie.

    Args:
        movies (dict): A dictionary containing movies as keys and their ratings as values.

    Returns:
        dict: The updated dictionary with the new rating.
    """
    movie = input("Enter movie name to update: ")
    if movie not in movies:
        print(f"\nMovie '{movie}' doesn't exist!")
    else:
        while True:
            try:
                new_rating = float(input("Enter new movie rating (0-10): "))
                if 0 <= new_rating <= 10:
                    print(f"\nMovie '{movie}' successfully updated")
                    movies[movie] = round(new_rating, 1)
                    return movies
                print(f"Rating {new_rating} is invalid. Please try again!")
            except ValueError:
                print("Invalid input. Please enter a number!")


def get_average_rating(movies: dict):
    """
    Calculates the average rating of all movies.

    Args:
        movies (dict): A dictionary containing movies as keys and their ratings as values.

    Returns:
        float: The average rating rounded to one decimal place.
    """
    return round(sum(movies.values()) / len(movies), 1)


def get_median_rating(movies: dict):
    """
    Calculates the median rating of all movies.

    Args:
        movies (dict): A dictionary containing movies as keys and their ratings as values.

    Returns:
        float: The median rating.
    """
    ratings = sorted(movies.values())
    mid = len(ratings) // 2
    return round(ratings[mid] if len(ratings) % 2 == 1 else (ratings[mid - 1] + ratings[mid]) / 2, 1)


def get_best_rated_movie(movies: dict):
    """
    Finds the highest-rated movie.

    Args:
        movies (dict): A dictionary containing movies as keys and their ratings as values.

    Returns:
        tuple: The name and rating of the highest-rated movie.
    """
    return max(movies.items(), key=lambda item: item[1])


def get_worst_rated_movie(movies: dict):
    """
    Finds the lowest-rated movie.

    Args:
        movies (dict): A dictionary containing movies as keys and their ratings as values.

    Returns:
        tuple: The name and rating of the lowest-rated movie.
    """
    return min(movies.items(), key=lambda item: item[1])


def get_random_movie(movies: dict):
    """
    Selects a random movie from the collection.

    Args:
        movies (dict): A dictionary containing movies as keys and their ratings as values.

    Returns:
        tuple: The name and rating of the randomly selected movie.
    """
    from random import choice
    return choice(list(movies.items()))


def find_movies(movies: dict):
    """
    Finds movies that contain a specific substring in their name.

    Args:
        movies (dict): A dictionary containing movies as keys and their ratings as values.

    Returns:
        dict: A dictionary of movies that match the search criteria.
    """
    part_of_movie_name = input("Enter part of movie name: ")
    return {
        key: value
        for key, value in movies.items()
        if part_of_movie_name.lower() in key.lower()
    }


def sort_movies_from_highest_to_lowest(movies: dict):
    """
    Sorts movies by their ratings in descending order.

    Args:
        movies (dict): A dictionary containing movies as keys and their ratings as values.

    Returns:
        dict: A dictionary of movies sorted by ratings from highest to lowest.
    """
    return dict(sorted(movies.items(), key=lambda item: item[1], reverse=True))


def main():
    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.5,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 4,
        "Forrest Gump": 6,
        "Star Wars: Episode V": 5
    }
    menu = ["List movies",
            "Add movie",
            "Delete movie",
            "Update movie",
            "Stats",
            "Random movie",
            "Search movie",
            "Movies sorted by rating"
            ]

    print_title("My Movie Database")

    while True:
        print_menu(menu)
        user_choice = ask_for_number()

        if user_choice == 1:
            show_all_movies(movies)
            if continue_or_quit():
                break
            continue
        elif user_choice == 2:
            add_movie(movies)
            if continue_or_quit():
                break
            continue
        elif user_choice == 3:
            delete_movie(movies)
            if continue_or_quit():
                break
            continue
        elif user_choice == 4:
            update_movie(movies)
            if continue_or_quit():
                break
            continue
        elif user_choice == 5:
            average_rating = get_average_rating(movies)
            median_rating = get_median_rating(movies)
            best_movie = get_best_rated_movie(movies)
            worst_movie = get_worst_rated_movie(movies)
            print(f"\n"
                  f"----- Stats -----"
                  f"\n"
                  f"Average rating: {average_rating}\n"
                  f"Median rating : {median_rating}\n"
                  f"Best movie    : '{best_movie[0]}', Rating: {best_movie[1]}\n"
                  f"Worst movie   : '{worst_movie[0]}', Rating: {worst_movie[1]}"
                  )
            if continue_or_quit():
                break
            continue
        elif user_choice == 6:
            random_movie = get_random_movie(movies)
            print(f"\n"
                  f"Your movie for tonight:\n"
                  f"'{random_movie[0]}', it's rated {random_movie[1]}")
            if continue_or_quit():
                break
            continue
        elif user_choice == 7:
            found_movies = find_movies(movies)
            print("\n")
            if found_movies == {}:
                print(f"No movie found.")
            else:
                print(f"Found movies: ")
                for movie, rating in found_movies.items():
                    print(f"'{movie}', Rating: {rating}")
            if continue_or_quit():
                break
            continue
        elif user_choice == 8:
            show_all_movies(sort_movies_from_highest_to_lowest(movies))
            if continue_or_quit():
                break
            continue


if __name__ == "__main__":
    main()
