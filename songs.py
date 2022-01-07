class Song(object):

    def __init__(self, title, song_id, uri, open_link):
        self.title = title
        self.song_id = song_id
        self.uri = uri
        self.open_link = open_link

    def parse_data(self):