def count_substring(string, sub_string):
    counter=0
    for c in range(len(string)-len(sub_string)+1):
        i=0
        status=True
        for c2 in range(len(sub_string)):
            if string[c+i]!=sub_string[c2]:
                status=False
            i += 1
        if status==True:
            counter += 1
    return counter
