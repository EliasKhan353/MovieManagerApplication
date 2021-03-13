# prompt the main user menu
MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

# empty dictionary to add movies
movies = []

# function to add movies
def add_movie():

    # take inputs for all the necessary details to add a movie
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    # add all the inputs in the empty dictionary
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

# function to see the list of movies
def show_movies():

    # loop runs from 0 to n where n is the last movie in the list
    for movie in movies:
        print_movie(movie)

# function to print all details of movies
def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print((f"Release year: {movie['year']}"))

# function to find movies
def find_movies():

    # initiate a variable with the search key word
    search_title = input("Enter the movie title you're looking for: ")

    # loop runs from 0 to n where n is the last movie in the list
    for movie in movies:

        # if the search key word is found, print all the details
        if movie["title"] == search_title:
            print_movie(movie)

# function for the user menu
def menu():

    # initiate a variable with the user choice
    selection = input(MENU_PROMPT)

    # run the loop and else-ifs to navigate different choice options
    while selection != 'q':
        if selection == "a":
            add_movie()
        elif selection == "l":
            show_movies()
        elif selection == "f":
            find_movies()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)

# run the menu function
menu()