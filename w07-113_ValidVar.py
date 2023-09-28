"""ValidVar"""
def check(time):
    """Check is hostname valid"""
    for _ in range(time):
        name = str(input())
        isok = "Valid"
        if name.isidentifier() == False:
            isok = "Invalid"
        if bool(name == "if") + bool(name == "else") + bool(name == "elif") + bool(name == "while")\
+ bool(name == "for") + bool(name == "True") + bool(name == "False") + bool(name == "continue")\
+ bool(name == "break") + bool(name == "return") + bool(name == "is") + bool(name == "in")\
+ bool(name == "and") + bool(name == "or") + bool(name == "from") + bool(name == "as")\
+ bool(name == "pass") + bool(name == "not") + bool(name == "def") + bool(name == "None"):
            isok = "Invalid"
        print(isok)
check(int(input()))
