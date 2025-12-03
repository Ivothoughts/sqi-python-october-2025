movie_genre = ("comedy", "romance", "thriller", "action", "adventure", "horror", "sci-fi", "anime", "muscical")

# upper_movie_genre = [movie.upper() for movie in movie_genre]

# print(upper_movie_genre)

# len_movie_genre = [movie for movie in movie_genre if len(movie) < 6]

# print(len_movie_genre)

# movie_genre = ("comedy", "romance", "thriller", "action", "adventure", "horror", "sci-fi", "anime", "muscical")

# movies = [len(movie) for movie in movie_genre]
# print(movies)
# print(movie_genre)
# movies.append(movie_genre)
# print(movies)

# movies = [ movies for movies in movie_genre]
# print(movies)

# for movie in movie_genre:

#     print(len(movie))

# # print(len(movie))

# all_countries = ["Nigeria", "USA", "Ghana", "UAE", "Canada", "Switzerland", "Japan", "Germany", "Australia", "Togo", "China"]

# developing_countries = ["Nigeria", "Togo", "Ghana"]

# developed_countries = [ countries for countries in all_countries if countries not in developing_countries]

# except_uae = [country for country in all_countries if country != "UAE"]

# # print(except_uae)

# # print(developed_countries)

# start_with_countries = {country: country.lower().startswith(("a", "e", "i", "o", "u")) for country in all_countries}

# print(start_with_countries)

# multiples = [number for number in range(1, 100) if number % 3 == 0 and number % 5 == 0]
# print(multiples)
# 1------------------------------
names = ["John", "Sara", "Mike", "Amanda"]

print([ name for name in names if "a" in name.lower() ])

# 2------------------------------
animals = ["dog", "cat", "lion", "tiger"]

print([animal[-1] for animal in animals ])

# 3---------------------
names = ["John", "Sara", "Mike", "Amanda"]
print(any(name for name in names if "a" in name.lower()))

# 4--------------------------------------
greetings = ["HELLO", "world", "pyTHon", "ROCKS"]

print(all(greeting == greeting.upper() for greeting in greetings))

print(all(greeting.isupper() for greeting in greetings))