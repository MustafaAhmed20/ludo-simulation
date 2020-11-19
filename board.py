def checkerboard(n, a, b):
	'''draw the game board
	perm n: the board size
	perm a: list of 'A' characters with postion in the path
	perm b: list of 'B' characters with postion in the path
	'''

	# the board . represented as list of lists
	board = [['']*(n+1)] *(n+1)

	# fixed width of the arm
	width = 3

	# the middle 
	middle = n // 2

	# the middle area
	middle_area = [middle-1, middle+1]

	# the First line
	# the horizontal numbers with shift in the left
	board [0] = [' '] + [str(i%10) for i in range(n)]
	
	for index, i in enumerate(range(n)):
		# tha main loop represent the vertical direction

		# the line list
		temp = []

		# the number on the left
		temp.append(str(index%10))

		# the up/down arm
		if index == 0 or i == n-1:
			temp.extend([i for i in ('*' * width).center(n,' ')])

		# the middle line
		elif index == middle:
			temp.extend([i for i in ('X'.center(n-2,'D').center(n, '*'))])

		# the middle area
		elif index in middle_area:
			temp.extend([i for i in (('D').center(n,'*'))])

		else:
			# the rest of the board
			temp.extend([i for i in (('*D*').center(n,' '))])
		
		
		# add the line to the board
		board[index+1] = temp


	# now insert the 'A' and 'B' characters
	# draw the "A"s and the "B"s
	try:
		for point in a:
			if point ==0 or point == -1:
				# 0 mean the point is not in the board
				continue
			i, j = getlocation(n, point, 'A')
			board[int(i)][int(j)] = 'A'
			

		for point in b:
			if point ==0 or point == -1:
				# 0 mean the point is not in the board
				continue
			i, j = getlocation(n, point, 'B')
			board[int(i)][int(j)] = 'B'
	except:
		print(f'i: {i}   j:{j}')
		raise e
	
	# print the board
	for line in board:
		print(' '.join(line))

def calculateFullPath(n):
	''' return the full path number of points. without the 'D' Area or "X" point
	perm n: the board size
	ex n = 9 -> 32
	'''

	horizontalWing = (n-1)/2
	verticalWing = horizontalWing -1
	
	# all the dots in the board - without the 'D' or the 'X'
	path = (4 * horizontalWing ) + (4 * verticalWing) + 4

	# cast it to int 
	return int(path)

def calculateWinPoint(n):
	''' return the number of points the character must move from the start to the end to win'''
	
	horizontalWing = (n-1)/2

	path = calculateFullPath(n)

	return path + horizontalWing

def getlocation(n, locationInPath, character):
	'''return (i,j) values represents the location of the point in the board.
	NOTICE i = vertical , j = horizontal
	perm n: the board size
	perm locationInPath: represents the character location in the path
	perm character: either 'A' or 'B' '''

	# first locate the character in the wings (ex horizontal - up - left)
	# the path starts at the left horizontal up wing

	# the path order is this
	#
	
	# 1. horizontal - up - left
	# 2. vertical - up - left
	# 3. center point - up
	
	# 4. vertical - up - right
	# 5. horizontal - up - right
	# 6. center point - right
	
	# 7. horizontal - down - right
	# 8. vertical - down - right
	# 9. center point - down
	
	# 10 vertical - down - left
	# 11 horizontal - down - left
	# 12 center point - left

	fullPath = calculateFullPath(n)

	# the middle 
	middle = (n // 2) + 1
	
	point1 = fullPath/4
	point2 = point1 * 2
	point3 = point1 * 3
	point4 = fullPath

	# this mean the character inside the 'D' area
	if (locationInPath < -1):
		if (character == 'A'):
			return(middle - (-1 - locationInPath), middle)
		else:
			return(middle + (-1 - locationInPath), middle)


	# the middle points
	if locationInPath == point1:
		# first point
		return (1, middle)
	
	if locationInPath == point2:
		# second pint
		return (middle, n)

	if locationInPath == point3:
		# third point
		return (n, middle)

	if locationInPath == point4:
		# forth point
		return (middle, 1)

	
	horizontalWing = (n-1)/2
	verticalWing = horizontalWing -1
	
	# 1. horizontal - up - left
	if 1 <= locationInPath <= horizontalWing :
		return (middle-1, locationInPath)
	
	# 2. vertical - up - left
	if horizontalWing < locationInPath < point1:
		return(point1-locationInPath, middle-1)
	
	# 4. vertical - up - right
	if point1 < locationInPath <= (point1 + verticalWing):
		return(locationInPath-point1, middle+1)

	lastIndex = n
	# 5. horizontal - up - right
	if locationInPath < point2:
		return (middle-1, lastIndex - (point2-locationInPath-1))
	
	# 7. horizontal - down - right
	if point2 < locationInPath <= (point2 + horizontalWing):
		return (middle+1, lastIndex - (locationInPath-point2-1) )
	
	# 8. vertical - down - right
	if locationInPath < point3:
		return (lastIndex - (point3-locationInPath-1), middle+1)
	
	# 10 vertical - down - left
	if point3 < locationInPath <= (point3+verticalWing):
		return (lastIndex -(locationInPath-point3-1), middle-1)

	# last section
	# 11 horizontal - down - left
	return (middle+1, point4-locationInPath)
