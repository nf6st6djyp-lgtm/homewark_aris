if __name__ == '__main__':
    N = int(input())
l=[]
for _ in range(N):
    command = input().split()  
    op = command[0]          
    if op == 'insert':
        i = int(command[1])
        e = int(command[2])
        l.insert(i, e)
    elif op == 'print':
        print(l)
    elif op == 'remove':
        e = int(command[1])
        l.remove(e)
    elif op == 'append':
        e = int(command[1])
        l.append(e)
    elif op == 'sort':
        l.sort()
    elif op == 'pop':
        l.pop()
    elif op == 'reverse':
        l.reverse()
