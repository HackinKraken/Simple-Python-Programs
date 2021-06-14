# This program says hello and asks for my name

print('Hello World')
print('What is your name?') # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print(('The length of your name is ') + (str(len(myName)) + (' characters long.')))
print('What is your age?') # ask for their age
myAge = input()
print(myName + ', you will be ' + str(int(myAge) + 1) + ' in a year.')
print('What is the single most important thing to you?') #ask what is important
impThing = input()
print((myAge + ' is a great age to be! Don\'t forget to exercise, eat healthy and spend time on ') + (impThing) + ('. Remember, that\'s important to you!'))
#Ask what kind of car I drive
print(('What kind of car do you drive, ') + myName + ('?'))
typeCar = input()
print(('That is an interesting choice. I always liked the reliability of a(n) ') + str(typeCar) + ('!'))
