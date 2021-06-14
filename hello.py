# This program says hello, asks for my name, tells me char length and asks about something important

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
