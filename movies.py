def print_title(title:str):
    print(f"********** {title} **********")

def print_menu(list_of_menu:list):
    print("\n")
    print("Menu:")
    for number, element in enumerate(list_of_menu):
        print(f"{number + 1}. {element}")
    print("\n")

def ask_for_number():
    while True:
        try:
            number = int(input("Enter choice (1-8): "))
            if 1 <= number <= 8:
                return number
            else:
                print("The choice must be between 1 and 8. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number!")
            continue

def continue_or_quit():
    print("\n")
    user_input = input("Press enter to continue or 'Q' to quit: ")
    if user_input == "q".lower():
        return True


def show_all_movies(dictionary:dict):
    print(f"\n----- Total of {len(dictionary)} movies -----\n")
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def add_movie(dictionary:dict):
    movie = input("Enter new movie name: ")
    if movie not in dictionary.keys():
        while True:
            try:
                rating = input("Enter new movie rating (0-10): ")
                if 0 <= float(rating) <= 10:
                    print(f"\n"
                          f"Movie '{movie}' (Rating: {rating}) successfully added")
                    dictionary[movie] = float(rating)
                    return dictionary
                else:
                    print(f"Rating {rating} is invalid. Please try again!")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number!")
                continue
    else:
        print(f"\n"
              f"'{movie}' already exist.")

def delete_movie(dictionary:dict):
    movie = input("Enter movie name to delete: ")
    if movie in dictionary.keys():
        print(f"\n"
              f"Movie '{movie}' successfully deleted")
        del dictionary[movie]
    else:
        print(f"\n"
              f"Movie '{movie}' doesn't exist!")
    return dictionary

def update_movie(dictionary:dict):
    movie = input("Enter movie name to update: ")
    if movie not in dictionary.keys():
        print(f"\n"
              f"Movie '{movie}' doesn't exist!")
    else:
        while True:
            try:
                new_rating = input("Enter new movie rating (0-10): ")
                if 0 <= float(new_rating) <= 10:
                    print(f"\n"
                          f"Movie '{movie}' successfully updated")
                    dictionary[movie] = round(float(new_rating), 1)
                else:
                    print(f"Rating {new_rating} is invalid. Please try again!")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number!")
                continue
            return dictionary

def get_average_rating(dictionary:dict):
    rating_sum = 0
    for rating in dictionary.values():
        rating_sum += rating
    return round(rating_sum / len(dictionary), 1)

def get_median_rating(dictionary:dict):
    median_list = []
    for value in dictionary.values():
        median_list.append(value)
    return sorted(median_list)[round(len(median_list) / 2)]

def get_best_rated_movie(dictionary:dict):
    highest_key = ""
    highest_value = 0
    for key, value in dictionary.items():
        if value > highest_value:
            highest_value = value
            highest_key = key
    return highest_key, highest_value

def get_worst_rated_movie(dictionary:dict):
    lowest_key = ""
    lowest_value = list(dictionary.values())[0]
    for key, value in dictionary.items():
        if value < lowest_value:
            lowest_value = value
            lowest_key = key
    return lowest_key, lowest_value

def get_random_movie(dictionary:dict):
    from random import choice
    key, value = choice(list(dictionary.items()))
    return key, value

def find_movies(dictionary:dict):
    part_of_movie_name = input("Enter part of movie name: ")
    found_items = {}
    for key, value in dictionary.items():
        if part_of_movie_name.lower() in key.lower():
            found_items[key] = value
    return found_items

def sort_movies_from_highest_to_lowest(dictionary:dict):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

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
                  f"----- Stats -----\n"
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