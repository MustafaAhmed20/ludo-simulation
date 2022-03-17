from odd import isBoardSizeValid
from play import *
import random

def rollTheDice():
	''' Roll the dice and return a random number between (1-6)'''
	return random.randint(1, 6)

if __name__ == '__main__':
	
	while True:
		# get the board size
		boardSize = input('Enter the board size (must be odd number): ')

		# boardSize must be odd number
		if isBoardSizeValid(boardSize):
			break

	# cast the input to int
	boardSize = int(boardSize)
		
	# play the Game
	#

	# this will be true if any player won
	win = False
	
	### the turn between the players - True mean A's turn
	turn = True
	

	# the players - 0 mean out of the board
	# 1 mean in the start place
	# -1 mean the stone already won
	# calculate the number of characters for every player with this formula
	A = [1] + [0] * ((boardSize - 3) // 2 - 1)
	B = [1] + [0] * ((boardSize - 3) // 2 - 1)

	

	defaultAGenerator = defaultA(boardSize)
	defaultBGenerator = defaultB(boardSize)
	
	print('-----------------------------------------------------------')
	print('---------------------Start the Game------------------------')

	while not win:
		# play till there is a winner
		
		# Roll the dice
		dice = rollTheDice()
		

		print(f'The score (characters won) from total {len(A)}\n A: {A.count(-1)}, B: {B.count(-1)}')
		print()
		print('The player turn is: ' + ('A' if turn else 'B'))
		print(f'The dice is {dice}')
		print()

		
		# play the game turn
		play(A, B, turn, dice, boardSize, next(defaultAGenerator), next(defaultBGenerator))
		

		# check if any player won
		win = all(map(lambda i: i == -1, A)) or all(map(lambda i: i == -1, B))
		
		
		print('-----------------------------------------------------------')

		# switch turn
		turn = not turn


	# won
	print('The Game Finished!!!')
	print('The winner is: ' + ('B' if turn else 'A'))