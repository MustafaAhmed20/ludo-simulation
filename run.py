from odd import checkOddInput
from play import *
import random

def rollTheDice():
	''' roll the dice and return a random number between (1-6)'''
	return random.randint(1, 6)

if __name__ == '__main__':
	
	while True:
		# get the n
		n = input('Enter the board size: ')
		if checkOddInput(n):
			break

	# cast the input to int
	n = int(n)
		
	# play the Game
	#

	win = False
	
	# the turn between the players - True mean A's turn
	turn = True

	# the players - 0 mean out of the board
	# 1 mean in the start place
	A = [1] + [0] * ( int( (n-3) // 2) -1 )
	B = [1] + [0] * ( int( (n-3) // 2) -1 )

	

	defaultAGenerator = defaultA(n)
	defaultBGenerator = defaultB(n)
	
	print('-----------------------------------------------------------')
	print('---------------------Start the Game------------------------')

	while not win:
		# play till there is a winner
		
		# roll the dice
		dice = rollTheDice()

		print(f'The score (characters won)\n A: {A.count(-1)}, B: {B.count(-1)}')
		print()
		print('The player turn is: ' + ('A' if turn else 'B'))
		print(f'The dice is {dice}')
		print()

		
		# play the game
		play(A, B, turn, dice, n, next(defaultAGenerator), next(defaultBGenerator))

		# check if the player won
		
		if all(map(lambda i: True if i == -1 else False, A)) or \
			all(map(lambda i: True if i == -1 else False, B)):
			win = True
		
		
		print('-----------------------------------------------------------')

		# switch turn
		turn = not turn


	# won
	print('The Game Finished!!!')
	print('The winner is: ' + ('B' if turn else 'A'))