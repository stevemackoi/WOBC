from sys import argv, stdout
from os import system, name

arg1 = abs(int(argv[1]))
null = None
pos = None

def clear_screen():
    system('cls' if name == 'nt' else 'clear')

def fibbCalc():
    n1, n2 = 0, 1
    count = 0
    nterms = 1000
    fibseq = []
    while count < nterms:
        fibseq.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    return fibseq

def which_fibonacci(a):
    fiblist = fibbCalc()
    found = arg1 in fiblist
    if found:
        pos = a.index(arg1)
        return pos + 1
    if not found:
        return 0

def next_fibonacci(a):
    found = arg1 in a
    if arg1 == 1:
        return 2
    if found:
        pos = a.index(arg1) + 1
        return a[pos]
    else:
        return 0

def main():
    fiblist = fibbCalc()
    print (which_fibonacci(fiblist))
    if (next_fibonacci(fiblist)) != 0:
        print (next_fibonacci(fiblist))

main()