"""
Objective
Today, we're learning about Key-Value pair mappings using a Map or Dictionary data structure.
Task
Given N names and phone numbers, assemble a phone book that maps friends' names
to their respective phone numbers. You will then be given an unknown number of names
to query your phone book for; for each name queried, print the associated entry from
your phone book (in the form name=number) or Not found if there is no entry for name.
Note: Your phone book should be a Dictionary/Map/HashMap data structure.
"""

phonebook = {}
entries = int(input())

for n in range(entries):
    name, num = input().strip().split(' ')
    name, num = [str(name), int(num)]
    phonebook[name] = num

while True:
    try:
        search = str(input())

        if search in phonebook:
            output = ''.join('%s=%r' % (search, phonebook[search]))
            print(output)
        else:
            print("Not found")
    except EOFError:
        break
 
