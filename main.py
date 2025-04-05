from functions import menu, print_title, print_menu, ask_for_valid_number, press_enter_to_continue, show_movies, \
    get_average_rating, get_median_rating, get_best_rated_movies, get_worst_rated_movies, \
    get_random_movie, find_movies, sort_movies_by_rating, get_title_from_user, \
    get_valid_rating_from_user, get_valid_year_from_user, sort_movies_by_year, ask_user_for_sequence, \
    display_movie_stats, display_found_movies, display_random_movie, get_minimum_rating_from_user, \
    get_start_year_from_user, get_end_year_from_user, filter_movies
from movie_storage import get_movies, delete_movie, add_movie, update_movie, save_movies


def main():
    print_title("My Movie Database")
    while True:
        print_menu(menu)
        user_choice = ask_for_valid_number(menu)
        movies = get_movies()
        if user_choice == 0:
            print("\nBye Bye!")
            break
        if user_choice == 1:
            show_movies(movies)
            press_enter_to_continue()
            continue
        elif user_choice == 2:
            new_movie_title = get_title_from_user()
            if new_movie_title not in movies["Title"]:
                add_movie(new_movie_title, get_valid_year_from_user(), get_valid_rating_from_user())
                press_enter_to_continue()
                continue
        elif user_choice == 3:
            delete_movie(get_title_from_user())
            press_enter_to_continue()
            continue
        elif user_choice == 4:
            update_movie(get_title_from_user(), get_valid_rating_from_user())
            press_enter_to_continue()
            continue
        elif user_choice == 5:
            display_movie_stats(get_average_rating(movies), get_median_rating(movies), get_best_rated_movies(movies),
                                get_worst_rated_movies(movies))
            press_enter_to_continue()
            continue
        elif user_choice == 6:
            display_random_movie(get_random_movie(movies))
            press_enter_to_continue()
            continue
        elif user_choice == 7:
            display_found_movies(find_movies(movies))
            press_enter_to_continue()
            continue
        elif user_choice == 8:
            show_movies(sort_movies_by_rating(movies, ask_user_for_sequence()))
            press_enter_to_continue()
            continue
        elif user_choice == 9:
            show_movies(sort_movies_by_year(movies, ask_user_for_sequence()))
            press_enter_to_continue()
            continue
        elif user_choice == 10:
            show_movies((filter_movies(movies, get_minimum_rating_from_user(), get_start_year_from_user(),
                                       get_end_year_from_user(), )))
            press_enter_to_continue()
            continue
    save_movies(movies)


if __name__ == "__main__":
    main()
