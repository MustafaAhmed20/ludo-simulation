def isBoardSizeValid(boardSize):
	''' check if the boardSize is valid
		return True if its valid number else false'''
	try:
		boardSize = int(boardSize)
	except Exception as identifier:
		return False

	# smallest board passible
	if boardSize < 5 :
		return False

	# check if this odd
	return boardSize % 2 != 0