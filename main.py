import requests
from bs4 import BeautifulSoup

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

# debug
# print(soup)
for song_title in song_titles:
    print((song_title.getText()).strip())
# print(song_artists[0])
