"""Run Length Decoding"""
def decode(text):
    """Decode to long string"""
    num = ""
    for char in text:
        if char.isdigit() == True:
            num += char
        else:
            word = char
        if char.isalpha() == True:
            print(word * int(num), end="")
            num = ""
decode(input())
