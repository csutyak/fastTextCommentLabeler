def fastTextAutoLabeler():

	import fasttext

	fileLabledComments = input("enter labeled comments file name: ")
	UnlabledComments = input("enter unlabeled comments file name: ")
	outputFile = input("enter output file name: ")

	print(fileLabledComments, "\n")
	classifier = fasttext.train_supervised(fileLabledComments, label_prefix="__label__", thread=8)

	output = open(outputFile, "a", encoding="utf8")
	readUnlabled = open(UnlabledComments, "r", encoding="utf8")
	lines = readUnlabled.readlines()
	for line in lines:
		line = line.replace('\n','')
		label = classifier.predict(line,k=1)
		output.write(label[0][0] + " " + line + '\n')

	print("Finished auto labeling comments ")
