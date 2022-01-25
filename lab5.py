import re 
file1 = open("keywords.txt", "r")
fileInfo = file1.read()
file1.close()
keywords=re.split("\s", fileInfo)
stream = ["far", "for","else", "If", "while"]
for i in stream:
	res = i in keywords
	if res :
		print(f"{i} is a keyword")
	else:
		print(f"{i} is not a keyword")

