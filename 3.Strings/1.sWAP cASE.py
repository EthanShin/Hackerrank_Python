def swap_case(s):
    ret = ''
    for i in s:
        if i.islower():
            ret += i.upper()
        elif i.isupper():
            ret += i.lower()
        else:
            ret += i
    return ret