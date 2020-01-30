import sys
from os import system

system('cls')

print (sys.argv[1] + " " + (sys.argv[2]))
print ((sys.argv[1])[0] + (sys.argv[2])[2] + (sys.argv[2])[-1] + str(len(sys.argv[2])))
print ()
print ()
print (len(sys.argv))
print ((sys.argv[1])[1:4])
print ("use of \'quotation\' marks")

userEnter = str(input("please enter: "))

print (userEnter[1])