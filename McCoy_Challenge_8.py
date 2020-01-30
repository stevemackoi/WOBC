def fileReader(x):

	with open(x) as f:
		openFile = (f.read())
		

		print (openFile)

fileReader('large.txt')