## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## class Dog has-a __init__ that takes self and name parameters 
class Dog(Animal):

	def __init__(self, name):
		# from self get the name attribute and set it to name
		self.name = name

## class Cat has a __init__ that takes self and name parameters
class Cat(Animal):

	def __init__(self, name):
		## ??
		self.name = name

## ??
class Person(object):

	def __init__(self, name):
		## ??
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## ??
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary

## ??
class Fish(object):
	pass

## ??
class Halibut(Fish):
	pass

## ??
class Salmon(Fish):
	pass


## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()

print frank.salary