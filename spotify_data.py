import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from secrets import CLIENT_SECRET, CLIENT_ID
from songs import Song

class SpotifyClient(object):

    def __init__(self):
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET
        self.auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        self.sp = spotipy.client.Spotify(auth_manager=self.auth_manager)

    def search_song(self, query_string):
        response = self.sp.search(q=query_string, type="track")
        print(response["tracks"]["items"][0]["external_urls"]["spotify"])

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

