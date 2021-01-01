class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def print_lyrics(self):
        for i in self.lyrics:
            print(i)
amelia_lyrics = ["I was driving across",
                "A burning desert",
                "When I spotted six"]

amelia = Song(amelia_lyrics)

in_your_eyes = Song(["love",
                    "I get so lost",
                    "Sometimes"])

amelia.print_lyrics()
in_your_eyes.print_lyrics()
