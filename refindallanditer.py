import re

def find_substrings(s):
    
    pattern = r'(?<=[qwrtpsdfghjklzxcvbnm])[aeiouAEIOU]{2,}(?=[qwrtpsdfghjklzxcvbnm])'
    
    matches = re.findall(pattern, s)
    
    if matches:
        for match in matches:
            print(match)
    else:
        print(-1)

s = input()
find_substrings(s)
