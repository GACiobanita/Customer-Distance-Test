filepath = input("Enter a file path or the program will use the default file:")
try:
    fhand = open(filepath)
except:
    print("Default file is used instead.") #if the input file path is wrong or the input is incorrect, or simply because the user wanted this to occur
    fhand = open("customers.txt")

count = 0  
for line in fhand:
    count+=1
print('There were', count, 'lines.')  