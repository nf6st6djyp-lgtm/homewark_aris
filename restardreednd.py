import re

s = input()
k = input()

pattern = f"(?=({re.escape(k)}))"

found= False
for m in re.finditer(pattern, s):
    print(((m.start()), m.end(1)-1))
    found = True

if not found:
    print((-1, -1))
