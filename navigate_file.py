enterfile = input("Enter the input file name: ")
file = open(enterfile, 'r')
linecount = 0
for line in file:
    linecount = linecount + 1
print("The file has",linecount,"lines.")
while True:
    linenum = 0
    num = int(input("Enter a line number [0 to quit]: "))
    if num >=1 and num <= linecount:
        file = open(enterfile, 'r')
        for lines in file:
            linenum = linenum + 1
            if linenum == num:
                print(num,":",lines)
    elif num == 0:
        break
    else:
        if num!= linecount:
            print("ERROR: line number must be less than",linecount)