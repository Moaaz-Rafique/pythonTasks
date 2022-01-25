def validate(s, c, n, currentIndex):
    print(f"\n{s},{currentIndex}", end=" ")       
    if len(s) < 1:
        return False
    if s[-1] == "$":
        if currentIndex == len(n) - 1:
            return True
    if s[-1] in c.keys():
        x = c[s[-1]]
        s.pop()
        for y in x:
            j = len(y) - 1
            i = len(y) - 1
            while i >= 0:
                ch = y[i]                
                s.append(ch)
                i = i - 1
            if validate(s, c, n, currentIndex):
                return True     
            else: 
                for k in range(j):
                    if(len(s)>1):
                        s.pop()      
        # s.pop()
        return False
    else:
        terminal = s.pop()
        if terminal == n[currentIndex]:
            currentIndex = currentIndex + 1
            return validate(s, c, n, currentIndex)
    return False


c = dict()
c["<S>"] = [["<SE>"],["K","i","a"," ","<SE>","?"] ]
c[("<SE>")] = [["<S1>"],["<S2>"], ["<S3>"],["<S4>"], ["<S5>"],  ]#
c[("<S1>")] = [["<IM>", "<MID>", "t", "a", " ", "h", "a", "i"]]  #[""],
c[("<S2>")] = [["<IF>", "<MID>", "t", "i", " ", "h", "a", "i"]]  #[""],
c[("<S3>")] = [["<IJ>", "<MID>", "t", "a", "y", " ", "h", "a", "i", "n"]]
c[("<S4>")] = [["<IPM>", "<MID>", "t","<T1>", " ", "h", "u", "n"]]  #[""],
c[("<S5>")] = [["<ISM>", "<MID>", "t", "<T2>", " ", "h", "o"]]  #[""],
c[("<IM>")] = [
                ['A', 'l', 'i'],
                ['H', 'a', 's', 'a', 'n'],
                ['M', 'o', 'a', 'a', 'z'], 
                ['Z', 'a', 'i', 'n'], 
            ]
c[("<IF>")] = [
                ['F', 'a', 't', 'i', 'm', 'a'],
                ['S', 'a', 'd', 'i', 'a'],
                ['B', 'i', 's', 'm', 'a'],
                ['J', 'a', 'm', 'e', 'e', 'l', 'a'],
                ["N", "i","m","r","a"]
            ]
c[("<IJ>")] = [["H", "u", "m"], ["V", "o"]]
c["<IPM>"] = [["H", "a", "i", "n"]]
c["<ISM>"] = [["T", "u", "m"]]
c["<MID>"] = [[" ", "<FAEL>"]]
c["<FAEL>"] = [['g', 'a', 'n', 'a', ' ', 'g', 'a'],['c', 'y', 'c', 'l', 'e', ' ', 'c', 'h', 'a', 'l', 'a'],['k', 'h', 'a', 'n', 'a', ' ', 'k', 'h', 'a'],
              ['b', 'a', 'z', 'a', 'r', ' ', 'j', 'a'],
              ['f', 'o', 'o', 't', 'b', 'a', 'l', 'l', ' ', 'k', 'h', 'e', 'l'],
              
              ['p', 'a', 'n', 'i', ' ', 'p', 'e', 'e'],
              ['k', 'h', 'a', 't', ' ', 'l', 'i', 'k', 'h'],
              ]
c[("<T1>")] = [["a"],["i"]]
c[("<T2>")] = [["a","y"],["i"]]
c[("$")] = [""]

inp = ['Kia Ali khana khata hai?$']#
#,"Tum gana gatay ho$","Nimra cycle chalati hai$", "Kia Sadia bazar jati hai?$","Kia Ali khana khata hai?$", "Hum bazar jatay hain$","Vo football kheltay hain$" 
ans=[]
for n in inp:
    s = ["$"]
    s.append("<S>")
    currentIndex = 0
    ans.append((n,validate(s,c,n,currentIndex)))
    print("\n\n")
for a in ans:
    print(a)