class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
	"I don''t want to get sued",
	"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
	"With pockets full of shells"])

duke_of_york = ["Oh, The grand old duke of York,",
"he had ten thousand men,",
"he marched them up to the top of the hill,",
"and he marched them down again"]


happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

york = Song(duke_of_york)

york.sing_me_a_song()

test = Song()
test.lyrics = ["Oh, The grand old duke of York,",
"he had ten thousand men,",
"he marched them up to the top of the hill,",
"and he marched them down again"]

test.sing_me_a_song()