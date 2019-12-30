#INF360-Programming in Python
#Catherine Schnelle
#Assignment 1

print('Hi there! Oh boy, I havent seen anyone for ages. What is your name?') #(print function) to display user greeting and prompt
myName = input()  #(input function) to store user input in variable
print('Nice to meet you ' + myName + '!') #(print function) to print contents of user input
print('My na...I do not have a name, actually. But I hear the others call me a "legacy program" sometimes.')
print('I must have left a great legacy!')
print('Well ' +myName+ ' you cannot walk around with a name like that in this day and age. I will tell you your cyberpunk name.')
print('Tell me the most recent fast food restaurant you patroned.')
myFood = input()
print('Great job! Now, tell me something you dont enjoy very much.')
myGrievances = input()
print('Welcome to the future '+myFood + myGrievances +'! I know you may prefer ' +myName+ 
' but this will serve you better when you inevitably become part machine!') #use of string concantenation 
print('Tell me your age.')
myAge = input()
print('Wow! You are ' +str(-int(myAge) +500) + ' years younger than me!') #two operators - and + used
print('Wait, what year do you think it is?')
myYear = input()
print('Oh boy, you are about ' +str(-int(myYear)+3000) + ' years off! It is the year 3000, silly goose!') #two operators - and + used
print('I have to go, nice talking to you!')
