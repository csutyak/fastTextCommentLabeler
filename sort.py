def sortFile():
	inputFileName = input("Enter Input File name to be sorted: ")
	f = open(inputFileName,  "r", encoding="utf8")
	lines = set(f.readlines())
	lines = sorted(lines)

	outputFileName = input("Enter Output File name to be sorted: ")

	output = open(outputFileName, "a", encoding="utf8")
	for line in lines:
		output.write(line)

	output.close()