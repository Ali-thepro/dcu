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
        self.d = {}

    def add(self, mp3):
        self.d[mp3.title] = mp3

    def remove(self, title):
        if title in self.d:
            del self.d[title]

    def lookup(self, title):
        if title in self.d:
            return self.d[title]
        else:
            return None
        
    def __add__(self, other):
        c = MP3Collection()
        for mp3 in self.d.values():
            c.add(MP3Track(mp3.title, mp3.duration, mp3.artists[:]))
        for mp3 in other.d.values():
            c.add(MP3Track(mp3.title, mp3.duration, mp3.artists[:]))
        return c