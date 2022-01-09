import spotipy
from spotipy.oauth2 import SpotifyOAuth
from secrets import *


class SpotifyClient(object):

    def __init__(self):
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET

        self.auth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                                         client_secret=CLIENT_SECRET,
                                         redirect_uri="http://example.com",
                                         username="310lggqfq3vyzqy6jznspvudqg4y",
                                         scope="playlist-modify-private")

        self.sp = spotipy.client.Spotify(auth_manager=self.auth_manager)

    def search_song(self, query_string):
        response = self.sp.search(q=query_string, type="track")
        print(response["tracks"]["items"][0]["external_urls"]["spotify"])

    def create_playlist(self, user_date):
        user = self.sp.current_user()["id"]
        name = f"{user_date} Billboard 100"
        self.sp.user_playlist_create(user=user, name=name,
                                     public=False, collaborative=False,
                                     description='A throwback playlist to make you feel nostalgic')

# create a new playlist
# user = "3GbPC5S4STGnDvihg4fHwTrxkVp229xjy6"
# name = "Songs-throwback"
# sp.user_playlist_create(user=user,
#                         name=name,
#                         public=False,
#                         collaborative=False,
#                         description='A throwback playlist to make you feel nostalgic')

# Add songs to playlist
# playlist_add_items(playlist_id, items, position=None)

# playlists = sp.user_playlists('spotify')
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None

# search for song

