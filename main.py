import requests
from bs4 import BeautifulSoup
from spotify_data import SpotifyClient

# user_date = input("Which year do you want to travel to? Please enter the date in this format YYYY-MM-DD:\n")
user_date = "2000-08-12"
# construct url
url = f"https://www.billboard.com/charts/hot-100/{user_date}"

# send request and capture response
response = requests.get(url)
webpage = response.text

# make soup
soup = BeautifulSoup(webpage, "html.parser")

# fetch songs
song_titles = soup.select(selector="ul li h3#title-of-a-story")
# song_artists = soup.select(selector="ul li span.c-label")

# get list of songs
list_of_songs = list()
for song_title in song_titles:
    list_of_songs.append((song_title.getText()).strip())

# search songs details on spotify using the above search query
sc = SpotifyClient()
for song in list_of_songs:
    query_string = f"{song} year:2000"
    try:
        sc.search_song(query_string)
    except IndexError:
        continue


# debug
# print(soup)

# print(song_artists[0])
