import sys
from os import system

system('cls')

first = int(sys.argv[1])
second = int(sys.argv[2])
third = str(sys.argv[3])

timeCheck = third.lower()

def highNumber(x, y):
    if x > y:
	    print (x)
    elif y > x:
	    print (y)

def oddThree(x, y):
	if ((x % 2 != 0) and (y % 2 != 0)) or ((x % 3 == 0) or (y % 3 == 0)):
		print (third)

highNumber(first, second)

if "time" in timeCheck:
	print (first + second)

oddThree(first, second)

if len(sys.argv) > 4:
    print ("error")