import fileinput
f=open('addFile.txt','r')
line=f.readlines()
filename='programFile.py'
for lines in fileinput.FileInput(filename,inplace=1):
	if '#add' in lines:
		lines = lines.rstrip()
		lines=lines.replace(lines, '\n'+s+'\n' )
