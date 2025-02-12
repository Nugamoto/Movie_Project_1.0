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
