greeting = "Good Morning"
name = "Harry"
# print(type(name))
concatenation = greeting + " "+name
print(concatenation)

# slicing
print(name[0])

# name[3]="a" # does not work

print(name[0:1])
print(name[0:2])
print(name[0:3])
print(name[0:4])
print(name[0:5])


#  advance techniques

print('''

''')

print(name[0:])  # same as name[0:5]
print(name[:5])
print(name[0:-1]+"y")
# reverse order

reverseString = "harry"


print(reverseString[-1])

print("reverse "+reverseString[-5:])


wordamazing = "awesome"
print(wordamazing[1::2])  # same as wordamazing[1:6:2]
