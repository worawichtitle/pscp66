"""Future Message"""
def message(text):
    """find type of text"""
    if text.isdigit():
        print("Number")
    elif text.isupper():
        print("Uppercase")
    elif text.islower():
        print("Lowercase")
    elif text.istitle():
        print("Title")
    elif text.isspace():
        print("Space")
    else:
        print("Other")
message(input())
