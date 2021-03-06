import random
import os
import time

class Board:

	__slots__ = ('tiles', 'LENGTH', 'SHOW', 'WIDTH', 'index', 'score')

	def __init__(self):
		self.LENGTH = 20
		self.SHOW = 4
		self.WIDTH = 4
		self.tiles = [[False for i in range(self.WIDTH)] for i in range(self.LENGTH)]
		self.index = 0
		self.setupBoard()

	def __str__(self):
		return "tiles: \n" + self.printBoard() + ", dimensions: " + \
		str(self.LENGTH) + " x " + str(self.WIDTH) + ", index: " + \
		str(self.index)

	def printBoard(self):
		s = "\n"

		for i in range(self.index - 1 + self.SHOW, self.index - 1, -1):

			if i >= self.LENGTH:
				s += "...."

			else:
				for tile in self.tiles[i]:
					s += "X" if tile else "."
			s += "\n"

		print(s)

	def setupBoard(self):
		for line in self.tiles:
			line[random.randint(0, self.WIDTH - 1)] = True

	def checkMove(self, move):
		if self.tiles[self.index][self.transform(move)]:
			self.index += 1
			return True
		else:
			return False

	def transform(self, move):
		if move == 'd':
			return 0
		elif move == 'f':
			return 1
		elif move == 'j':
			return 2
		elif move == 'k':
			return 3

	def endGame(self):
		return self.index == self.LENGTH

# Main program.
def main():
	board = Board()
	get = _Getch()
	first = True

	while not board.endGame():
		os.system('cls')
		board.printBoard()

		c = str(get())[-2]

		if first:
			startTime = time.time()
			first = False

		if not board.checkMove(c):
			print("You lose!")
			printTimeStats(board, startTime, False)
			return

	os.system('cls')
	board.printBoard()
	print("You win!")
	printTimeStats(board, startTime, True)


def printTimeStats(board, startTime, won):
	totalTime = time.time() - startTime
	print(("Lasted " if not won else "Did ") + str(board.index) + " moves, took " + "{0:.3f}".format(totalTime) + " seconds")
	print("Keys per second: " + "{0:.3f}".format((float(board.index) / totalTime) if totalTime != 0 else 0))
	checkHighScore(totalTime, won)

def checkHighScore(time, won):
	openfile = open("hiscore.txt", "w+")
	hiscore = 99999999999999999999
	if openfile is not None:
		hiscore = float(openfile.readline())

	if time < hiscore and won:
		print("New hiscore!")
		openf = open("hiscore.txt", "w")
		openf.write(str(time))
		openf.close()
	else:
		print("Current hiscore: " + str(hiscore))

class _Getch:
    """
    Gets a single character from standard input.  Does not echo to the
    screen.
    """
    def __init__(self):
        self.impl = _GetchWindows()

    def __call__(self): return self.impl()

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

main()