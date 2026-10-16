def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        sb=string[i:i+k]
        visited=[]
        outp=[]
        for c in sb:
            if c not in visited:
                visited.append(c)
                outp.append(c)
        print("".join(outp))
    