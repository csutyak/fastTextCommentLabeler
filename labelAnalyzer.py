# shows statistics on the labels of comments in a dataset

def labelAnalyzer():
	
	import numpy as np

	commentFileName = input("enter file name of labeled comments: ")

	catagories = []
	commentLabelConfigFileName = 'commenLabelConfig.txt'
	commentLabelConfig = open(commentLabelConfigFileName, 'r', encoding="utf8") 
	commentLabelConfigLines = commentLabelConfig.readlines()
	# get the latest line count
	lineCount = 0
	for line in commentLabelConfigLines:
	    if line:
	        catagories.append(line.strip("\n"))

	npArraySize = []
	for catagory in catagories:
		npArraySize.append(0)

	labelQuantityArr = np.array(npArraySize)
	lineCtr = 0
	file = open(commentFileName, "r", encoding="utf8")
	for line in file.readlines():
	    labelQuantityArr[int(line[9]) - 1] = labelQuantityArr[int(line[9]) - 1] + 1
	    lineCtr += 1

	

	ctr = 0
	for catagory in catagories:
		print("Label ", catagory, ": ", labelQuantityArr[ctr])
		ctr += 1
