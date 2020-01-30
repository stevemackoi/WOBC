import sys
from os import system

system('cls')

first = (int(sys.argv[1]) + 1)

def userRange(y):
	i = 1
	for x in range(y):
	    if (x % 12 == 0) and (x != 0):
	    	print (str(i) + "dozen")
	    	i = i+1
	    elif (x % 3 == 0) and (x != 0):
	    	print ("triangle")
	    elif (x % 4 == 0) and (x != 0):
	    	print ("square")

userRange(first)

my_list = list(range(1, first))

print (sum(my_list))

