"""Run Length Encoding"""
def encode(text):
    """Encoding the text"""
    count = ""
    nowchar = ""
    code = ""
    for char in text:
        if char != nowchar:
            code += str(count) + nowchar
            count = 1
            nowchar = char
        else:
            count += 1
    code += str(count) + nowchar
    print(code)
encode(str(input()))
