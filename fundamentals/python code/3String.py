a="Hello, World!!"
print(a)

print("Hello" in a) # will print true or false

print("Hello" not in a)

# slicing
print(a[2:5])
print(a[:5])
print(a[5:])
print(a[:-1])

# upper case
print(a.upper())

# lower case
print(a.lower())

# strip
print(a.strip()) # remove space from starting and ending

print(a.replace('l','ani')) #will replace l with 'ani'

print(a.split(',')) #if no value is provided for split it will split on basis of space

# concatenation
b=" Animesh"
c=a+b;
print(c)

# F string
age=23
str=f"I am {age} year old"
print(str)

# capitalize
# count() returns number of times a specified value occurs in a string
# encode() returns encoded version of the string
# find() searches the string for a specified value and returns the position of where it was found
# isnumeric()
# islower()

print(bool("abs"))