
class MP3Track(object):

    def __init__(self, title, duration, artists):
        self.title = title
        self.duration = duration
        self.artists = artists


    def __str__(self):
        output = []
        output.append(f'Title: {self.title}')
        output.append(f'By: {", ".join(self.artists)}')
        output.append(f'Duration: {self.duration}')
        return "\n".join(output)
    
class MP3Collection(object):

    def __init__(self):
        self.tracks = {}

    def add(self, mp3):
        self.tracks[mp3.title] = mp3

    def remove(self, title):
        if title in self.tracks:
            del self.tracks[title]

    def lookup(self, title):
        if title in self.tracks:
            return self.tracks[title]
        else:
            return None
        
    def __add__(self, other):
        new_collection = MP3Collection()
        for track in self.tracks.values():
            if track.title not in new_collection.tracks:
                new_collection.add(track)
        for track in other.tracks.values():
            if track.title not in new_collection.tracks:
                new_collection.add(track)