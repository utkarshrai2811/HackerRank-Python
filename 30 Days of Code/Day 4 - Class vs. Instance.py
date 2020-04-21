"""
In this challenge, we're going to learn about the difference between a class and an instance;
because this is an Object Oriented concept, it's only enabled in certain languages.
Task
Write a Person class with an instance variable, age, and a constructor that takes an integer, initialAge, as a parameter.
The constructor must assign initialAge to Age after confirming the argument passed as _initialAge is not negative.
If a negative argument is passed as initialAge, the constructor should set to and print "Age is not valid, setting age to 0."
In addition, you must write the following instance methods:
	age_1_year() should increase the instance variable Age by 1.
	is_old() should perform the following conditional actions:
		If age < 13, print "You are young.".
		If age >= 13 and age < 18, print "You are a teenager.".
		Otherwise, print "You are old.".
"""


class Person:
	# Add some more code to run some checks on initialAge
	def __init__(self, initialAge):
		if initialAge < 0:
			print("Age is not valid, setting age to 0.")
			self.Age = 0
		else:
			self.Age = initialAge

	# Do some computations in here and print out the correct statement to the console
	def is_old(self):
		if self.Age < 13:
			print("You are young.")
		elif (13 <= self.Age) and (self.Age < 18):
			print("You are a teenager.")
		else:
			print("You are old.")

	# Increment the age of the person in here
	def age_1_year(self):
		self.Age += 1


T = int(input())

for i in range(0, T):
	age = int(input())
	p = Person(age)
	p.is_old()
	for j in range(0, 3):
		p.age_1_year()
	p.is_old()
	print("")
