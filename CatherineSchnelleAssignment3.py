# INF360 Programming in Python
# Catherine Schnelle
# Week 3 Assignment

#- Initial comments*
#- Use at least 2 comparison operators.
#- Use at least 1 boolean operator (and, or, not).
#- Write at least 1 if statement that contains 2 elif statements and 1 else statement.
#- Write at least 1 while statement that contains a break and continue.
#- Write at least 1 for loop using the range() method.
#- Use the import keyword to import the random module. Use the random.randint() function somewhere in your script.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
			 ['Alice', 'Bob', 'Carol', 'David'],
			 ['dogs', 'cats', 'moose', 'goose']]
			 
#printTable function
def printTable(tableData):

    #creates list containing same # of 0s as lists in tableData.
	colWidths = [0] * len(tableData)
	
    #while loop sets i to 0 then compares it to the length of tableData list, then  
    #increments until colWidths equal to max length in tableData
	i=0
	while i < len(tableData):
		colWidths[i] = len(max(tableData[i], key = len))
		i=i + 1
		
    #finds largest value in colWidths list to pass that integer to the right justify method. 
	for i in range(len(tableData[0])):
		for j in range(len(colWidths)):
			print(tableData[j][i].rjust(colWidths[j]), end=' ')
		print(end='\n')
printTable(tableData)