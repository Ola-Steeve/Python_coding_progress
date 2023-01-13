"""##The beginning of the mosh python coding tutorial
print('Hello world')
print('*' * 10)

##VARIABLES

price =100
print(price)

##Patient details

patint = 'john smith'
patient_age = 24
is_new = True

####Getting input

name = input('Enter your name: ')
Age = input('How old are you?: ')
color = input('what is your favourite color?: ')
print(f'Hello {name}, you are {Age} yars old and your favourite color is {color}')


##Type conversion

birth_year = input('Birth year: ')
age = 2023 - int(birth_year)
print(f'you are {age} years old')   
print(type(birth_year))
print(type(age))


"""
###Excersice 
User =input('Your weight: ')
conv =input('lb or kg: ').lower()
if conv == 'lb':
    weight = int(User) * 0.454
    print(f'Your weight in Kg is {weight}kg')
else:
    weight = float(int(User) /0.454)
    print(f'Your weight in Lb is {weight}Lb')


##STRINGS
course ='Python coding'

course1="Python's course for ""Beginners" 
course2="""

python's course for "beginners" """

print(course, course1, course2)
print(course[0])
print(course[0:4])
print(course[4:])
print(course[:])
another =course[:]




