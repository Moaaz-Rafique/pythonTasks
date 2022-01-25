# z = 0
# i = 0
# j = 0
# c = 0

# a=["\0"] * 5
# ac=["\0"] * 5
# stk=["\0"] * 5
# act=["\0"] * 5
# def check():
#     global z,c,i,j,a,ac,stk,act

#     for z in range(c):
#         if stk[z] == "i":
#             print("reduced to E->i")
#             stk[z]="E";
#             stk[z+1] = "\0";
#             print(f"${stk}\t${a}")
#     for z in range (c-2):
#         if stk[z] == "E" and stk[z+1]=="+" and stk[z+2]=="E":
#             print("reduce to E->E+E")
#             stk[z] = "E";
#             stk[z+1] = "\0"
#             stk[z+2] = "\0"
#             print(f"${stk}\t${a}")
#     return

# a = list("i+i+i")

# c = len(a)
 
# i=0
# while(j<c):
    
#     print(act)
#     stk[i] = a[j]
#     stk[i+1] ="\0"
#     a[j]=" "
#     print(f"{stk}\t{a}")
#     check()
# if(stk[0] == "E" and stk[1]=="\0"):
#     print("Aceept")
# else:
#     print("Regect")



#     i=i+1
#     j=j+1

            


n = list("i+i")
n.append(None)
n.append(None)
n.append(None)
n.append(None)
i = 0
l = len(n)+5
st=[None]*l

def check():        
    global i,st
    print(i)
    if st[i] == "i":
        st[i]="E"
        print("reduced from E->i",st[i])
        i=i+1
        print(st)
    elif st[i]=="E" and st[i-2] =="E":
        st[i]=None
        st[i-1]=None
        print("reduced from E->E+E|E->E*E")
        i = i-1
        print(st)
    else:
        i=i+1
        print(st)
    
while True:
    st[i]=n[i]-
    # print("shift ", st[i], n)
    print(n)
    check()
    if st[i] == "E" and st[i+1]==None:
        break
check()

print("Accepted")