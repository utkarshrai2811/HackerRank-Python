class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximum_difference = 0
    # Add your code here

    def compute_difference(self):
        l = len(a)
        for i in range(0, l):
            for j in range(i + 1, l):
                difference = abs(a[i] - a[j])
                self.maximum_difference = max(
                    difference, self.maximum_difference)

# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.compute_difference()

print(d.maximum_difference)
