filepath = input("Enter a file path or the program will use the default file:")
try:
    fhand = open(filepath)
except:
    print("Default file is used instead.") #if the input file path is wrong or the input is incorrect, or simply because the user wanted this to occur
    fhand = open("customers.txt") #takes the same amount of time regardless of file size

count = 0
userID = 0
name = "Unknown"
lat = 0
lon = 0
for line in fhand:
    lineContents=line.split(',')
    
    pos = lineContents[0].find(':')
    lat = float(lineContents[0][pos+3:len(lineContents[0])-1])
    
    pos = lineContents[3].find(':')
    lon = float(lineContents[3][pos+3:len(lineContents[3])-1])