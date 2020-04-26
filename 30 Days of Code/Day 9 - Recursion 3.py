"""
Objective
Today, we're learning and practicing an algorithmic concept called Recursion.
Task
Write a factorial function that takes a positive integer, N as a parameter and prints the result of N!(N factorial).

Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.
"""

def factorial(n):
	if n == 0:
	return 1
	else:
	return n * factorial(n - 1)


n = int(input())
print(factorial(n))
