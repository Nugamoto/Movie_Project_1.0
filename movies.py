from functions import menu, movies, print_title, print_menu, ask_for_number, press_enter_to_continue, show_all_movies, \
    add_movie, \
    delete_movie, update_movie, get_average_rating, get_median_rating, get_best_rated_movie, get_worst_rated_movie, \
    get_random_movie, find_movies, sort_movies_from_highest_to_lowest


def main():
    print_title("My Movie Database")

    while True:
        print_menu(menu)
        user_choice = ask_for_number()

        if user_choice == 0:
            print("\nBye!")
            break
        if user_choice == 1:
            show_all_movies(movies)
            press_enter_to_continue()
            continue
        elif user_choice == 2:
            add_movie(movies)
            press_enter_to_continue()
            continue
        elif user_choice == 3:
            delete_movie(movies)
            press_enter_to_continue()
            continue
        elif user_choice == 4:
            update_movie(movies)
            press_enter_to_continue()
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
            press_enter_to_continue()
            continue
        elif user_choice == 6:
            random_movie = get_random_movie(movies)
            print(f"\n"
                  f"Your movie for tonight:\n"
                  f"'{random_movie[0]}'\nIt's rated {float(random_movie[1]["Rating"])} "
                  f"and released {random_movie[1]["Year of release"]}.")
            press_enter_to_continue()
            continue
        elif user_choice == 7:
            found_movies = find_movies(movies)
            print("\n")
            if found_movies == {}:
                print(f"No movie found.")
            else:
                print(f"Found movies: ")
                for movie, data in found_movies.items():
                    print(f"'{movie}' | Rating: {float(data["Rating"])}")
            press_enter_to_continue()
            continue
        elif user_choice == 8:
            show_all_movies(sort_movies_from_highest_to_lowest(movies))
            press_enter_to_continue()
            continue


if __name__ == "__main__":
    main()
