filepath = input("Enter a file path or the program will use the default file:")
try:
    fhand = open(filepath)
except:
    print("Default file is used instead.") #if the input file path is wrong or the input is incorrect, or simply because the user wanted this to occur
    fhand = open("customers.txt") #takes the same amount of time regardless of file size

remove = str.maketrans(dict.fromkeys(' :"'))#create a dictionary from keys, then create a table "remove"

count = 0
userID = 0
name = "Unknown"
lat = 0
lon = 0
for line in fhand:
    lineContents=line.split(',')
    
    pos = lineContents[0].find(':')
    tempVal = lineContents[0][pos:len(lineContents[0])-1]
    tempVal = tempVal.translate(remove) #use the table to create a new string, we still use tempVal in this case, removing the characters in the table from the string
    lat = float(tempVal)                #this could be futher extended to also remove all the letters from the start, leaving us only the numbers we need in the sections of the list we are interested
    
    pos = lineContents[3].find(':')
    tempVal = lineContents[3][pos:len(lineContents[3])-1]
    tempVal = tempVal.translate(remove)
    lon = float(tempVal)

