def fizz_buzz(x):
	'''
	fizz_buzz returns 'FizzBuzz' when a multiple of 3 and 5 is given,
	'Fizz' when a multiple of 3 is given and 'Buzz' when a multiple of
	5 is given

	'''

	# check for argument data type
	if type(x) == str:
		
		# raise Exception
		return x


	# first check defines whether x is divisible by both 3 and 5 with a remainder of 0
	if x % 3 == 0 and x % 5 == 0:
		return 'FizzBuzz'

	# second check defines whether x is divisible by 5 with a remainder of 0
	elif x % 5 == 0:
		return 'Buzz'

	# third check defines whether x is divisible by 3 with a remainder of 0
	elif x % 3 == 0:
		return 'Fizz'
	
	else:
		return x

fizz_buzz('20')