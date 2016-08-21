import unittest
from fizz_buzz import fizz_buzz


def empty_arg():
	raise Exception('Provide one argument')


def string_arg(fizz):
	raise Exception('Provide a numerical value')


class FizzTest(unittest.TestCase):

	def test_for_empty_arg(self):
		with self.assertRaises(Exception) as context:
			empty_arg()
		self.assertTrue('Provide one argument' in context.exception)


	def test_for_string_arg(self):
		with self.assertRaises(Exception) as context:
			string_arg()
		self.assertFalse('Provide a numerical value' in context.exception)


	def test_for_fizz1(self):
		self.assertEquals(fizz_buzz(9), 'Fizz',  msg="Should return 'Fizz' for multiples of 3")


	def test_for_fizz1(self):
		self.assertEquals(fizz_buzz(27), 'Fizz',  msg="Should return 'Fizz' for multiples of 3")


	def test_for_buzz1(self):
		self.assertEquals(fizz_buzz(10), 'Buzz',  msg="Should return 'Buzz' for multiples of 5")


	def test_for_fizzbuzz(self):
		self.assertEquals(fizz_buzz(15), 'FizzBuzz',  msg="Should return 'FizzBuzz' for multiples of both 3 and 5")


	def test_for_fizzbuzz(self):
		self.assertEquals(fizz_buzz(90), 'FizzBuzz',  msg="Should return 'FizzBuzz' for multiples of both 3 and 5")


	def test_for_inapplicable(self):
		self.assertEquals(fizz_buzz(26), 26, msg='Should return value if not divisible by both 3 and 5')


	def test_for_validity(self):
		self.assertTrue(fizz_buzz(15), 'FizzBuzz')


	def test_for_argument(self):
		self.assertNotIsInstance(fizz_buzz('Fizz'), int, msg="Input an integer")


	def test_int_argument(self):
		x = 10
		self.assertTrue(type(x), int, msg="Provide integer argument")


if __name__=='__main__':
	unittest.main()