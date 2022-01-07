import requests
from bs4 import BeautifulSoup


class Billboard(object):

    def __init__(self, url):
        self.url = url
        self.list_of_songs = list()

    def get_songs(self):
        response = requests.get(self.url)
        webpage = response.text
        # make soup
        soup = BeautifulSoup(webpage, "html.parser")
        song_titles = soup.select(selector="ul li h3#title-of-a-story")
        for song_title in song_titles:
            self.list_of_songs.append((song_title.getText()).strip())

        return self.list_of_songs
