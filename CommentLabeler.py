# Script for automating the labling of comments

# get the amount of lines read for saving. 
# Using readlines() 

commentDataFileName = input("Please enter filename for unlabled comments: ")

while True:   # repeat until the try statement succeeds
    try:
        allComments = open(commentDataFileName, "r", encoding="utf8")
        break
    except IOError:
        commentDataFileName = input("Could not open file! Please enter a valid filename for unlabed Comments: ")
        # restart the loop

commentCasheFileName = 'CommentCache.txt'
commentCashe = open(commentCasheFileName, 'r', encoding="utf8") 
commentCasheLines = commentCashe.readlines()
# get the latest line count
lineCount = 0
for line in commentCasheLines:
    if line:
        lineCount = int(line)

print("Starting from line: ", lineCount)

# appends text to file on a new line
def appendLine(fileName, text):
    file = open(fileName, "a", encoding="utf8")
    if(text[-1] == '\n'): 
        file.write(text)
    else:
        file.write(text + '\n')
    file.close()

labelOutputFileName = "commentsLabeled.txt"

#1 for great comment
#2 for bad comment :(
#3 for not definable
catagories = ["1","2","3"]
categoryPrefix = "__label__"
workingLineCtr = 0

allCommentLines = allComments.readlines()

for commentLine in allCommentLines:

    if workingLineCtr >= lineCount:
        # delete comment markers
        workingCommentLine = commentLine
        if workingCommentLine[1] == "*":
            workingCommentLine = workingCommentLine[:-4]
        workingCommentLine = workingCommentLine[3:]

        loopFlag = True
        while loopFlag:
            print(workingCommentLine)
            userInput = input("input category for comment: ")
            if userInput in catagories:
                workingCommentLine = categoryPrefix + userInput + " " + workingCommentLine
                appendLine(labelOutputFileName, workingCommentLine)
                loopFlag = False
            elif userInput.lower() == "exit":
                appendLine(commentCasheFileName, str(workingLineCtr))
                exit()
            else:
                print("ERROR: PLEASE INPUT PROPER CATEGORY OR 'exit' TO EXIT")

    workingLineCtr += 1

print("End Of File!")