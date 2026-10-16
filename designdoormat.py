if __name__== "__main__":
    l=input().split(" ")
    n=int(l[0])
    m=int(l[1])

for i in range(1,n,2):
    print((".|."*i).center(m,"-"))
    
print("WELCOME".center(m,"-"))

for i in range(n-2,0,-2):
   print((".|."*i).center(m,"-"))
    