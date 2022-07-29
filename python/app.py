def maximum(a = 0, b =0, c=0):
    if a>=b and a>=c:
        return a
        
    if a<c and b<c: 
        return c
    if b>a and b>c:
        return b