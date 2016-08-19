


class Car(object):

	
	def __init__(self, name, model, type, speed=0, num_of_doors=0, num_of_wheels=0, parked_speed = 0, moving_speed = 0):
		super(Car, self).__init__()
		self.name = name
		self.model = model
		self.type = type
		self.speed = speed
		self.num_of_doors = num_of_doors
		self.num_of_wheels = num_of_wheels
		self.parked_speed = parked_speed
		self.moving_speed = moving_speed



	def is_saloon(self):
		if self.num_of_doors <= 5:
			return 'saloon'
		return 'trailer'
