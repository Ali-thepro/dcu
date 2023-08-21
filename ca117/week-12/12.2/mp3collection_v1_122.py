class MP3Track(object):

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        output = []
        output.append(f'Title: {self.title}')
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