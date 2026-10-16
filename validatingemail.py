import re
import email.utils

n = int(input())

# Regex for valid email:
pattern = re.compile(
    r'^[a-zA-Z][a-zA-Z0-9._-]*'  # username
    r'@'
    r'[a-zA-Z]+'                 # domain
    r'\.'
    r'[a-zA-Z]{1,3}$'            # extension (1-3 letters)
)

for _ in range(n):
    line = input().strip()
    name, email_addr = email.utils.parseaddr(line)  # extract name, email

    if pattern.match(email_addr):
        print(line)
