# nterms = int(input("How many terms? "))
# # first two terms
# n1, n2 = 0, 1
# count = 0
# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1


def which_fibonacci(x):
  count = 0
  n1, n2 = 0, 1
  numberList = []
  if x < 0:
    print("Sorry, No Negative Numbers")
  elif nterms < 100:
      while count < (100):
          #print(n1)
          nth = n1 + n2
          # update values
          n1 = n2
          n2 = nth
          numberList.append(n1)
          count += 1
      else:
          #print (numberList.index(nterms))
          #answer = numberList.index(nterms)
          #print (answer)
          print (numberList)
          # for i in [i for i, x in enumerate(numberList) if x == (nterms)]:
          #   print (i)
          #   #0 1 1 2 3 5 8 13


nterms = int(input("What is the magic number? "))

which_fibonacci(nterms)