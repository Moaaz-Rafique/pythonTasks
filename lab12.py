from beautifultable import BeautifulTable
import re

from matplotlib.pyplot import table

inp = "main ( ) { int i ; float j ; { int k ; float i ; } }"  #input('Enter your input ,separated by space : ')
dt = ['init','int', 'char', 'string', 'double', 'float']
tab = []
tok = []
tok = open("lab6LexicalAnalizer/lexemes.txt", "r").read()
tok = tok.split('\n')
tokArray = []
for i in range(len(tok)):
    x = tok[i][2:-2].split(r",")
    tokArray.append(x)
# print(tokArray)
# print(tok, "\n")
tok=tokArray
tab=[]    

def lookup(name, scope):
    for x in tab:
        if(x[0]==name):
            return True
    return False
def main():
    # print("main")
    scope=0
    table=BeautifulTable()
    error=False
    i=0
    while i < len(tok):
        if tok[i][0] in ["Keyword"]:
            # print(tok[i], "is valid")
            i=i+1
            continue
        elif tok[i][0] in ["Init"]:
            i=i+1
            if tok[i][0] in ["Identifier"]:                
                if not lookup(tok[i][1], scope):
                    i=i+1
                    if tok[i][0] in ["Assignment"]:
                        i=i+1
                        if tok[i][0] in ["Literal"]:               
                            tab.append([tok[i-2][1], tok[i][0], scope, tok[i][1]])   
                            table.rows.append([tok[i-2][1], tok[i][0], scope, tok[i][1]])
                        else: 
                            print("Expected literal and found", tok[i])
                    else: 
                        print("Expected = and found", tok[i])
                else:
                    print(tok[i], "is already defined")                    
            else:
                print ("init must be followed by identfier", i, tok[i])
        elif tok[i][0] in ["Identifier"]:
            if lookup(tok[i][1], scope):
                print(tok[i][1], "is used", i)            
            else:
                print(tok[i], "is not defined", i)
        i=i+1        

    print("\nSymbol Table")
    print(table)
main()

