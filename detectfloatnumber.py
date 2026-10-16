if __name__=="__main__":
    n=int(input())
    s=[]
    for _ in range(n):
       s.append(input())
       
def cnum(n):
    try:
         float(n)
         return True
    except ValueError:
        return False     
for n in s:
    state=True
    if n.count(".")!=1:
        state=False
    if n[0]not in "+-.0123456789":
        state=False
    if cnum(n)==False:
        state=False
    print(state)


    
