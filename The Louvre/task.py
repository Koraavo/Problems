class Painting:

    def __init__(self, title, artist, year):
        self.artist = artist
        self.title = title
        self.year = year

    def print_sta(self):
        print(f'"{self.title}" by {self.artist} ({self.year}) hangs in the Louvre.')


paintings = Painting(input(), input(), input())
paintings.print_sta()
