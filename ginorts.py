s = input()
lower = []
upper = []
odd = []
even = []

for c in s:
    if c.islower(): 
        lower.append(c)
    elif c.isupper():  
        upper.append(c)
    elif c.isdigit(): 
        if int(c) % 2 == 0:  
            even.append(c)
        else: 
            odd.append(c)


l = sorted(lower)
u = sorted(upper)
o = sorted(odd)
e = sorted(even)

print("".join(l) + "".join(u) + "".join(o) + "".join(e))
