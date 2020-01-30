import sys
import string

def fn(s):
  order = []
  counts = {}
  for x in (s.upper()):
    if x in counts:
      counts[x] += 1
    else:
      counts[x] = 1 
      order.append(x)
  for x in order:
    if counts[x] == 1:
      #return True
      print(x)
      break

if len(sys.argv) < 2:
  print (""" \n"" """)

else:
  fn (sys.argv[1])

