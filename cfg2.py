def validate(s, c, n, currentIndex):   
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
        # return False
    else:
        terminal = s.pop()
        if terminal == n[currentIndex]:
            currentIndex = currentIndex
            return validate(s, c, n, currentIndex + 1)
    return False



c = dict()
c["<S>"] = [["K","i","a"," ","<SE>","?"], ["<SE>"],]
c[("<SE>")] = [["<S1>"],["<S2>"], ["<S3>"],["<S4>"], ["<S5>"], ]#
c[("<S1>")] = [["<IM>"," ", "<LP1>"]]  #[""],
c[("<S2>")] = [["<IF>"," ", "<LP2>"]]  #[""],
c[("<S3>")] = [["<IJ>"," ", "<LP3>"]]
c[("<S4>")] = [["<IPM>"," ", "<LP4>"]]  #[""],
c[("<S5>")] = [["<ISM>"," ", "<LP5>"]]  #[""],

c[("<LP1>")] = [["<MID>","t", "a",  " ","h", "a", "i"],["<NMID>", "t", "a",]]
c[("<LP2>")] = [["<MID>","t", "i", " ", "h", "a", "i"],["<NMID>", "t", "i",],]
c[("<LP3>")] = [[ "<MID>", "t", "a", "y", " ", "h", "a", "i", "n"],["<NMID>", "t", "a", "y"],]
c[("<LP4>")] = [["<MID>", "t","<T1>",  " ","h", "u", "n"],["<NMID>", "t","<T1>"],]  #[""],
c[("<LP5>")] = [["<MID>",  "t", "<T2>",  " ","h", "o"],["<NMID>", "t", "<T2>"],]  #[""],

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
c["<NMID>"] = [
                ['g', 'a', 'n', 'a', ' ','n','h','i',' ', 'g', 'a'],
              ['c', 'y', 'c', 'l', 'e', ' ', 'n','h','i',' ','c', 'h', 'a', 'l', 'a'],              
              ['k', 'h', 'a', 'n', 'a', ' ','n','h','i',' ', 'k', 'h', 'a'],
              ['b', 'a', 'z', 'a', 'r', ' ', 'n','h','i',' ','j', 'a'],
              ['f', 'o', 'o', 't', 'b', 'a', 'n','h','i',' ','l', 'l', ' ', 'k', 'h', 'e', 'l'],
              
              ['p', 'a', 'n', 'i', ' ','n','h','i',' ', 'p', 'e', 'e'],
              ['k', 'h', 'a', 't', ' ', 'n','h','i',' ','l', 'i', 'k', 'h'],
]
c["<MID>"] = [['g', 'a', 'n', 'a', ' ', 'g', 'a'],
              ['c', 'y', 'c', 'l', 'e', ' ', 'c', 'h', 'a', 'l', 'a'],              
              ['k', 'h', 'a', 'n', 'a', ' ', 'k', 'h', 'a'],
              ['b', 'a', 'z', 'a', 'r', ' ', 'j', 'a'],
              ['f', 'o', 'o', 't', 'b', 'a', 'l', 'l', ' ', 'k', 'h', 'e', 'l'],
              
              ['p', 'a', 'n', 'i', ' ', 'p', 'e', 'e'],
              ['k', 'h', 'a', 't', ' ', 'l', 'i', 'k', 'h'],
              ]
c[("<T1>")] = [["a"],["i"]]
c[("<T2>")] = [["a","y"],["i"]]
c[("$")] = [""]

inp = ["Nimra khelne jata hai","Tum gana nhi gatay","Nimra cycle chalati hai", "Kia Sadia bazar jati hai?","Kia Ali khana khata hai?", "Hum bazar jatay hain","Vo football kheltay hain","Hum khelne jati hai"]#
#
ans=[]
for n in inp:
    n+="$"
    s = ["$"]
    s.append("<S>")
    currentIndex = 0
    if validate(s,c,n,currentIndex):
        print (n[:-1], " is valid grammar")
    else:
        print (n[:-1], " is invalid grammar")

    
print()
for a in ans:
    print(a)