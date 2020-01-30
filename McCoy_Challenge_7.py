import sys

def counts(x):
	string = (x)
	stringList = []
	stringList.extend(string)
	str_counts = dict((s, stringList.count(s)) for s in set(stringList))
	print (str_counts)

counts(sys.argv[1])