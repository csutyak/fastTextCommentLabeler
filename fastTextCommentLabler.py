#main driver code for the comment labler tool
from CommentLabeler import CommentLabeler
from sort import sortFile
from labelAnalyzer import labelAnalyzer
from fastTextAutoLabeler import fastTextAutoLabeler

#main loop
while(True):
	userInput = input("enter command: ")

	if userInput == "help":
		print("list of commands:")
		print("help - help")
		print("quit - quit")
		print("labelComments - runs comment labeler")
		print("sortFile - runs a script to sort a file")
		print("labelAnalyzer - runs labelAnalyzer")
		print("autoLabeler - runs FastTextAutoLabeler")
	elif userInput == "quit":
		break
	elif userInput == "labelComments":
		CommentLabeler()
	elif userInput == "sortFile":
		sortFile()
	elif userInput == "labelAnalyzer":
		labelAnalyzer()
	elif userInput == "autoLabeler":
		fastTextAutoLabeler()
	else:
		print("please enter a valid command, help for help")

print("shell terminating")