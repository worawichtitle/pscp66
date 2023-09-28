"""Bad Keyboard"""
def hrun(text):
    """Replace o with i and i with o"""
    fix = ""
    for word in text:
        if word == "i":
            fix += "o"
        elif word == "I":
            fix += "O"
        elif word == "o":
            fix += "i"
        elif word == "O":
            fix += "I"
        else:
            fix += word
    print(fix)
hrun(str(input()))