class MP3Track(object):

    def __init__(self, title, duration, artists):
        self.title = title
        self.duration = duration
        self.artists = artists


    def __str__(self):
        output = []
        output.append(f'Title: {self.title}')
        output.append(f'By: {", ".join(self.artists)}')
        m, s = to_min_secs(self.duration)
        output.append(f'Duration: {m:01d}:{s:02d}')
        return "\n".join(output)

def to_min_secs(s):
    # m = s // 60
    # s = s % 60
    m, s = divmod(s, 60)
    return m, s
