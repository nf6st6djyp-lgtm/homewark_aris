import re

def valid_card(card):
    
    if "-" in card:
        for group in card.split("-"):
            if len(group)!=4:
                return "Invalid"
            
        c=card.replace("-","")
    else:
        c=card
        
    if c[0] not in "4,5,6":
        return "Invalid"
     
    if len(c)!=16:
        return "Invalid"
     
    if c.isdigit()==False:
        return "Invalid"
    
    if (re.search(r'(.)\1\1\1', c)):
        return "Invalid"
    
    return "Valid"

n = int(input())
for _ in range(n):
    card = input()
    print(valid_card(card))
