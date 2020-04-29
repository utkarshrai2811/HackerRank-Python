"""
Objective
Today, we're delving into Inheritance.
Task
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. 
Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student 
inherits all the properties of Person.
"""


class Person:
	def __init__(self, first_name, last_name, id_number):
            self.first_name = first_name
            self.last_name = last_name
            self.id_number = id_number

	def printPerson(self):
            print("Name:", self.last_name + ",", self.first_name)
            print("ID:", self.id_number)


class Student(Person):
	def __init__(self, first_name, last_name, id_number, scores):
            super().__init__(first_name, last_name, id_number)
            self.scores = scores

	def calculate(self):
            a = sum(self.scores) / len(self.scores)
            if a < 40:
                return "T"
            elif (40 <= a) and (a < 55):
                return "D"
            elif (55 <= a) and (a < 70):
                return "P"
            elif (70 <= a) and (a < 80):
                return "A"
            elif (80 <= a) and (a < 90):
                return "E"
            elif (90 <= a) and (a <= 100):
                return "O"
            else:
                return ""


line = input().split()
first_name = line[0]
last_name = line[1]
idNum = line[2]
numScores = int(input())
scores = list(map(int, input().split()))
s = Student(first_name, last_name, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
