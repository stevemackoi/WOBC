import sys
from os import system

system('cls')

first = int(sys.argv[1])
second = int(sys.argv[2])
third = float(sys.argv[3])

print (str(first + second) + " " + str(first * third) + " " + str(first % second) + " " + str(third // first))
first += 1
second += 1
third += 1
print (str(first >> 3) + " " + str(second / 2) + " " + str(first | second))
print (first + (len(sys.argv) - 1))