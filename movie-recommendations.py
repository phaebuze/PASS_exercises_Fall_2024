def recommend_movie(genre):
    if genre == "Comedy":
        movie = "Toy Story"

    elif genre == "Romance":
        movie = "The Notebook"

    elif genre == "Horror":
        movie = "Harry Potter"

    elif genre == "Sci-fi":
        movie = "Star Wars"

    elif genre == "Drama":
        movie = "Parasite"
        
    else:
        movie = "Genre doesn't match"

    return movie


genre = input("Enter a movie genre for a recommendation. 'quit' to quit. ")

while genre != "quit":
    movie = recommend_movie(genre)
    print("Movie recommendation based on " + genre + " is: " + movie)
    
    genre = input("Enter a movie genre for a recommendation. 'quit' to quit. ")

print("Bye")
