import random
import os
import time

class Board:

	__slots__ = ('tiles', 'LENGTH', 'WIDTH', 'index', 'score')

	def __init__(self):
		self.LENGTH = 20
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
		for i in range(self.LENGTH - 1, self.index - 1, -1):
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

# Main program.
def main():
	board = Board()
	get = _Getch()
	startTime = time.time()
	won = True

	for i in range (board.LENGTH):
		os.system('cls')
		board.printBoard()
		if not board.checkMove(str(get())[-2]):
			print("You lose!")
			won = False
			printTimeStats(board, startTime)
			break

	if won:
		print("You win!")
		printTimeStats(board, startTime)

def printTimeStats(board, startTime):
	totalTime = time.time() - startTime
	print("Lasted " + str(board.index) + " moves, took " + str(totalTime) + " seconds")
	print("Keys per second: " + str(float(totalTime) / (board.index + 1.0)))

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