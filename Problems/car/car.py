from abc import ABCMeta, abstractmethod

class Vehicle(object):


	 __metaclass__ = ABCMeta

	
	def __init__(self, name, model, type, speed=0, honk, num_of_doors=0, num_of_wheels=0, parked_speed = 0, moving_speed = 0):
		super(Vehicle, self).__init__()
		self.name = name
		self.model = model
		self.type = type
		self.speed = speed
		self.honk = honk
		self.num_of_doors = num_of_doors
		self.num_of_wheels = num_of_wheels
		self.parked_speed = parked_speed
		self.moving_speed = moving_speed



	def is_saloon(self):
		if self.num_of_doors <= 5:
			return 'saloon'
		return 'trailer'

	def sale_price(self):
		if self.sold_on is not None:
			return 0.0
		return 5000.0 * self.num_of_wheels


	def honk(self):
		pass


	@abstractmethod
	def vehicle_category(self):
		
		pass