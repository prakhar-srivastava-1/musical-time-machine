class Song(object):

    def __init__(self, title, song_id, uri, open_link):
        self.title = title
        self.song_id = song_id
        self.uri = uri
        self.open_link = open_link

    def get_attrib(self, attrib):
        if attrib == "id":
            return self.song_id
        elif attrib == "uri":
            return self.uri
        elif attrib == "link":
            return self.open_link
