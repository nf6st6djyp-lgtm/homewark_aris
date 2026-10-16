def mutate_string(string, position, character):
    stringa= string[0:position]+character+string[position+1:len(string)+1]
    return stringa

