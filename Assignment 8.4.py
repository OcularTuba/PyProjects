#Open the file romeo.txt and read it line by line.
#For each line, split the line into a list of words using the split() method.
#The program should build a list of words.
#For each word on each line check to see if the word is already in the list and if not append it to the list.
#When the program completes, sort and print the resulting words in alphabetical order.
#(https://www.py4e.com/code3/romeo.txt)


fname = input('Enter file name: ')
fhand = open(fname)
nline = list()
for ln in fhand :
    ln = ln.rstrip()
    line = ln.split()
    nline = nline + line
eline = list()
for x in nline :
    if x not in eline :
        eline.append(x)
        eline.sort()
print(eline)
