def fS(A, s, e):
    
    p = s + int((e - s) / 2)
    print(f"{s}-{e},{p}")
    if e==s:
        return f"{A[s]}  at {s} eq"
    if e<s:
        return f"{A[s]}  at {s} ind"
    if p<e and A[p + 1] < A[p]:
        return f"{A[p+1]}  at {p+1} p+1"
    
    if p>s and A[p] < A[p - 1]:
        return f"{A[p]}  at {p} p-1"
    elif A[e] < A[p]:
        return fS(A, s, p - 1)
    
    return fS(A, p + 1, e)

 
# A = [ 9,7,4,2,1]

A = [ 1,2,3,4,5]
print (fS(A, 0, len(A)-1))
