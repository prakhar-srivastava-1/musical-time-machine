from spotify import SpotifyClient
from billboard import Billboard

# user_date = input("Which year do you want to travel to? Please enter the date in this format YYYY-MM-DD:\n")
user_date = "2000-08-12"
year = user_date.split("-")[0]
year = year.strip()
# construct url
url = f"https://www.billboard.com/charts/hot-100/{user_date}"

# crate Billboard object
billboard = Billboard(url)
# send request and capture response
list_of_songs = billboard.get_songs()

# search songs on spotify using search query
sc = SpotifyClient()
for song in list_of_songs:
    query_string = f"{song} year:{year}"
    try:
        sc.search_song(query_string)
    except IndexError:
        continue


# debug
# print(soup)

# print(song_artists[0])
