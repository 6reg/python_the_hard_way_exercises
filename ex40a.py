class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"])

bulls_on_parade = Song(["The rally around the family",
    "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

me_oh_my = Song(["Oh me", "Oh my", "Oh me oh my"])

me_oh_my.sing_me_a_song()


lyrics = ["oh me", "oh my", "oh me oh my"]

me_oh_my = Song(lyrics)

me_oh_my.sing_me_a_song()