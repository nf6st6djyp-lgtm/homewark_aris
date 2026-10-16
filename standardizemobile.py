def wrapper(f):
    def fun(l):
        cleaned = [phone[-10:] for phone in l]
        formatted = [f"+91 {num[:5]} {num[5:]}" for num in cleaned]
        f(formatted)
    return fun