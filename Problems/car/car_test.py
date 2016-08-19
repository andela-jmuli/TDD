import unittest
from car import Car




class CarTest(unittest.TestCase):


	def test_car_type(self):
		gallardo = Car('gallardo', 'spider', 'saloon')
		self.assertTrue(gallardo.is_saloon(), msg='The type should be a saloon')


	def test_car_property(self):
		nissan = Car('nissan', 'xtrail', 'saloon')
		self.assertListEqual(['nissan', 'xtrail'],[nissan.name, nissan.model], msg='Car properties should be valid')


	def test_car_wheels(self):
		toyota = Car('toyota', 'hiace', 'saloon')
		canter = Car('mitsubishi', 'cantter', 'truck')
		self.assertListEqual([4, 6],[toyota.num_of_wheels, canter.num_of_wheels], msg='The car shoud have at least 4 wheels unless its a truck')


	def test_car_doors(self):
		toyota = Car('toyota', 'hiace', 'saloon')
		canter = Car('mitsubishi', 'cantter', 'truck')
		self.assertListEqual([4, 3],[toyota.num_of_wheels, canter.num_of_wheels], msg='The car shoud have at least 5 doors unless its a truck')




if __name__=='__main__':
	unittest.main()