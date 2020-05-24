f=open('addFile.txt','r')
lines=f.readlines()
f.close()

str=" "
str=str.join(lines)

import fileinput
file = "programFile.py"
for line in fileinput.FileInput(file, inplace=1):
    if '#' in line:
        line = line.replace(line,str+'\n')
    print(line,)
