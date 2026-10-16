def minion_game(string):
    stuart = 0
    kevin = 0
    n = len(string)

    for i in range(n):
        
        if string[i] in "AEIOU":
            kevin += n - i  
        else:
            stuart += n - i  
    
    if stuart == kevin:
        print("Draw")
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Kevin", kevin)

