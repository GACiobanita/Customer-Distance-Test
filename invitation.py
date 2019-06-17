import distanceCalculation as dCalc
import mergeSort as mSort
from timeit import default_timer as timer #for time measurement of the running program

filepath = input("Enter a file path or the program will use the default file:")
try:
    fhand = open(filepath)
except:
    print("Default file is used instead.") #if the input file path is wrong or the input is incorrect, or simply because the user wanted this to occur
    fhand = open("customers.txt") #takes the same amount of time regardless of file size

remove = str.maketrans(dict.fromkeys('""}{'))#create a dictionary from keys, then create a table "remove"

startTime = timer() #added a timer to check for algorithm speed, Visual Studio Code does not have "CPU Usage" feature

count = 0
userID = 0
name = "Unknown"
lat = 0
lon = 0
invList = list()

for line in fhand:
    line = line.strip()
    line = line.translate(remove)
    lineContents=line.split(',') # list of 4 elements: {lat_0, user_id_1, name_2, lon_3}

    pos = lineContents[0].find(':')
    tempVal = lineContents[0][pos+1:len(lineContents[0])]
    lat = float(tempVal)                
    
    pos = lineContents[3].find(':')
    tempVal = lineContents[3][pos+1:len(lineContents[3])]
    lon = float(tempVal)

    dist = dCalc.calculate_distance(lat, lon)

    if dist <= 100.0 :    
        pos = lineContents[1].find(':')
        tempVal = lineContents[1][pos+1:len(lineContents[1])]
        userID=int(tempVal)
        
        pos = lineContents[2].find(':')
        tempVal = lineContents[2][pos+2:len(lineContents[2])] #+2 to remove an additional space before the name
        name = tempVal

        invList.append((userID, name))

mSort.mergeSort(invList)
print("Time to complete this run was:", timer()-startTime)
for elem in invList:
    print(elem)    
