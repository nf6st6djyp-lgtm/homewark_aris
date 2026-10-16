import string

def print_rangoli(n):
    alphabet = string.ascii_lowercase
    width = n * 4 - 3
    lines = []
    
    for i in range(n):
        s = "-".join(alphabet[i:n])
        lines.append((s[::-1] + s[1:]).center(width, "-")) 
    
    lines.reverse()
    print("\n".join(lines + lines[:-1][::-1]))