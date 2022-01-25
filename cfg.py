def validate(s,c,n,currentIndex):
    # print(f"\n{s},{currentIndex}", end=" ")       
    
    if len(s) < 1: 
        return [False]
    if s[-1] == "$": 
        if currentIndex == len(n)-1:
            return [True,s,currentIndex]
        else:
            return [False,s,currentIndex]
    if s[-1] in c.keys():               
        x=c[s[-1]]
        s.pop()
        for y in x:           
            i=len(y)-1     
            while i >= 0:
                ch = y[i]
                # print(ch)   
                # if ch == "":
                #     print("\n-----------empty------------\n")   
                #     i = i-1  
                #     break
                if ch in 'x':
                    s.append("")
                    i=i-1    
                    continue
                if ch in '>':
                    ch = y[i-2:i+1]
                    i=i-2        
                # print(x, end=" appending ")                
                s.append(ch)    
                i=i-1
            # print(f"after append {s}")            
            if validate(s,c,n,currentIndex)[0]:        
                return [True,s,currentIndex] 
        if(len(s)>1):         
            s.pop()
        # print(("from s",s))
        return [False,s,currentIndex]                        
    else:
        terminal=s.pop()
        # print(f"pree{terminal}, {s}, {n[currentIndex]}")
        if terminal == n[currentIndex]:
            currentIndex = currentIndex +1        
            return validate(s,c,n,currentIndex)          
        elif terminal == "":            
            currentIndex = currentIndex - 1  
            return validate(s,c,n,currentIndex)  
        elif not terminal:
            print(("t",terminal))
            # print(("s",s))
            # return validate(s,c,n,currentIndex)  
    return [False,s,currentIndex]       

    

c = dict()

c[("<S>")] = [["<A>"],["<A>","<B>"]]
c[("<A>")] = [ ["e"],["a","<A>"],["a"],]#[""],
c[("<B>")] = [["b"],["b","<B>"]]
c[("$")] = [""]
# c["<E>"] = [["<T>", "<D>"]]
# c["<D>"] = [["+","<T>", "<D>"]]
# c["<T>"]= [["<F>", "<S>"]]
# c["<S>"]= [["*","<F>", "<S>"]]
# c["<F>"]= [["a"],["1"]]
# c[("$")] = [" "]


inp = ["aeea$"]# "$","abbbb$",,"aaabbb$","aaab$","aba$","abc$", "aab$", "b$", "bbbb$"

ans=[]
for n in inp:
    s = ["$"]
    s.append("<S>")    
    currentIndex = 0
    ans.append((n,validate(s,c,n,currentIndex)))
    # print("\n\n")
for a in ans:
    print(a)