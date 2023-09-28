"""Password"""
import math
def password(text):
    """Find a STRONG<oOo> password"""
    l_val = len(text)
    r_val = pool(text)
    entropy = int(math.log((r_val**l_val), 2))
    print(entropy)
    print(strong(entropy))
 
def pool(text):
    """Find Pool"""
    lowchar = False
    bigchar = False
    number = False
    specail = False
    for word in text:
        if word.islower():
            lowchar = True
        elif word.isupper():
            bigchar = True
        elif word.isdigit():
            number = True
        elif word.isidentifier() == False or word == "_":
            specail = True
    poolval = bool(lowchar) * 26 + bool(bigchar) * 26 + bool(number) * 10 + bool(specail) * 32
    return poolval
 
def strong(ent):
    """Grade How STRONG <oOo> password"""
    if 28 > ent:
        return "Very Weak"
    elif 35 >= ent >= 28:
        return "Weak"
    elif 59 >= ent >= 36:
        return "Reasonable"
    elif 127 >= ent >= 60:
        return "Strong"
    elif ent >= 128:
        return "Very Strong"
 
password(str(input()))
