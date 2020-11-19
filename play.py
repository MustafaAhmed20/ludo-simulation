from board import checkerboard, calculateFullPath, calculateWinPoint

def defaultA(n):
	'''calculate the default 'A' position in the path
	perm n: the size of the board
	return a nubmer which is the default postion for 'A' character
	NOTICE: this is a generator - will calculate once '''

	from board import calculateFullPath
	
	path = calculateFullPath(n)
	
	# 'A' postion is after point 1
	point1 = int( path//4 )

	# use yield to calculate the value only once
	while True:
		yield point1 + 1

def defaultB(n):
	'''calculate the default 'B' position in the path
	perm n: the size of the board
	return a nubmer which is the default postion for 'B' character
	NOTICE: this is a generator - will calculate once '''

	from board import calculateFullPath
	
	path = calculateFullPath(n)
	
	# 'A' postion is after point 3
	point1 = int( path//4 )
	point3 = point1 *3

	# use yield to calculate the value only once
	while True:
		yield point3 + 1

def chooseCharacter(player, dice, fullPath):
	''' choose the next character will be played
	perm player: the list of the player characters
	perm dice : the random dice number
	perm fullPath: the full path include 'D' area and 'X' point

	return the index of the character chosen
	return -1 if no character can be moved'''

	def validMove(character, dice, fullPath):
		''' check if this character can move with dice
			return True if valid else False'''
		if character == -1:
			# already won
			return False
		
		if character == 0:
			# can't move until the dice is 6
			return False

		# the character in 'D' area
		if character < -1:
			if (character + dice) <= -1:
				return True
			else:
				return False
		
		if character + dice <= fullPath:
			return True

		
		return False


	# try take out character from the house
	if dice == 6:
		for index, i in enumerate(player):
			if i == 0:

				# if there is not any other valid move - take character out without the user permission
				if not any(map(lambda p: validMove(p, dice, fullPath), player)):
					player[index] = 1
					# no move
					return -1

				else:
					# ask the user if want to get out a character from the house
					while True:
						answer = input(
							"do you want to take out a character from the house or want to move ? (o, m)\n")
						if answer.lower() == 'o' or answer.lower() == 'm':
							break
					
					# take out the character
					if answer.lower() == 'o':
						player[index] = 1
						# no move
						return -1
					else:
						# the user choose to move
						# break the loop in line 74
						break
	
	
	# if no valid move for the characters on the board
	if not any(map(lambda p: validMove(p, dice, fullPath), player)):
		return -1

	# if there is a multi available characters
	multiCharacter = False
	count = 0
	
	
	for index, i in enumerate(player):
		if validMove(i, dice, fullPath):
			count +=1
	
	if(count > 1):
		multiCharacter = True
	
	# choose Character to move
	if multiCharacter:
		player.sort(reverse=True, key = lambda a: a*-10000 if a <-1 else a)
		
		validMoveIndexes =[]
		for index, i in enumerate(player):
			if validMove(i, dice, fullPath):
				validMoveIndexes.append(index)
		
		# ask the user to choose
		while True:
			answer = input("choose character to move from " + ','.join([str(i+1) for i in validMoveIndexes]) + " (1 is the more advanced)\n")
			try:
				answer = int(answer)
			except Exception as e:
				continue
			
			# must be valid input and valid move for the chosen character
			if answer in range(1, len(player)+1) and validMove(player[answer-1], dice, fullPath):
				# valid answer
				return answer -1

	# this mean only one character can move with valid move
	for index, i in enumerate(player):
		if i > 0 or i < -1:
			return index

	# no character can move
	# just to be sure
	return -1

def play(A, B, turn, dice, n, defaultA, defaultB):
	''' play the game.
	perm A: the A characters postions
	perm B: the B characters postions
	perm turn: a bollean - true mean A's turn
	perm dice: a number between (1-6)
	perm n: the board size
	perm defaultA: the default location of A character in the path
	perm defaultB: the default location of B character in the path
	
	no return from this function - it modify the A and B lists
	'''

	def getTheRealLocation(point, default, fullPath):
		''' calculate the real location of the character in the board
			perm fullPath: the full path without the 'D' area '''
		# 0 mean out of the board
		# -1 mean won
		# < -1 mean in the 'D' area
		if point < 1:
			return point
		
		# decrease one, because one in the A or B mean the first place
		point += default -1 
		point %= fullPath

		# don't return 0
		return point if point else 1

	def exit():
		''' draw the board and exit'''
		ATemp = [getTheRealLocation(i, defaultA, fullPath) for i in A]
		BTemp = [getTheRealLocation(i, defaultB, fullPath) for i in B]

		# draw the board
		checkerboard(n, ATemp, BTemp)

	fullPathToWin = calculateWinPoint(n)
	fullPath = calculateFullPath(n)

	player = None
	other = None

	# Determine the player
	player, other = (A, B) if turn else (B, A)

	# choose Character that will move
	playerIndex = chooseCharacter(player, dice, fullPathToWin)
	
	if playerIndex ==-1:
		# no charecter out for some reason
		# don't move a thing
		
		exit()
		return

	
	# this mean the charecter compleated the path - Enter the 'D' area
	if player[playerIndex] + dice > fullPath:
		D = fullPath - player[playerIndex] + 1
		dice -= D
		# first D place
		player[playerIndex] = -1 - ( ((n-1)//2) - 1)
	
	
	# move the charecter in the path
	player[playerIndex] += dice

	# get the real location of the characters in the board
	ATemp = [getTheRealLocation(i, defaultA, fullPath) for i in A]
	BTemp = [getTheRealLocation(i, defaultB, fullPath) for i in B]

	# check if the new move of the player killed one of the other
	if player is A:
		if ATemp[playerIndex] in BTemp and ATemp[playerIndex] > 1:
			# A killed B
			killedIndex = BTemp.index(ATemp[playerIndex])
			# the other's character get out of the board
			other[killedIndex] = 0
			BTemp[killedIndex] = 0

	else:
		if BTemp[playerIndex] in ATemp and BTemp[playerIndex] > 1:
			# B killed A
			killedIndex = ATemp.index(BTemp[playerIndex])
			# the other's character get out of the board
			other[killedIndex] = 0
			ATemp[killedIndex] = 0

	exit()

