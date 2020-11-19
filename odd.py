def checkOddInput(number):
	''' check if the number is odd
		return True if its odd number else false'''
	try:
		number = int(number)
	except Exception as identifier:
		return False

	if number < 5 :
		# smallest board passible
		return False

	# check if this odd
	return number%2 != 0