#!/usr/bin/python3
"""Reading the Dracula"""


with open("dracula.txt", "r") as redFile:
    # set the count variable
    vamCount = 0
    #  redFile = redFile.readlines()
    for redLine in redFile:
        if "vampire" in redLine.lower():
            vamCount += 1
           # print(redLine)
    projectLine = "the total of lines with \"vampire\" in it are " + str(vamCount)
    #print(projectLine) 
    
    resultData = redLine + projectLine
    print(resultData)

    #, " lines", file=vampytimes.txt)
    #with open("vampytimes.txt", "w") as vampy:
    #print("the total of lines with \"vampire\" in it are ", vamCount) , " lines", file=vampytimes.txt)


   
