"""Align"""
def aligntext():
    """Set text to align with place you want"""
    size = int(input())
    place = input().lower()
    text = input()
    if place == "left":
        print(text + " " * (size - len(text)))
    elif place == "center":
        if (size - len(text)) % 2 != 0:
            print(" " * (((size - len(text)) // 2) + 1) + text + " " * ((size - len(text)) // 2))
        else:
            print(" " * ((size - len(text)) // 2) + text + " " * ((size - len(text)) // 2))
    elif place == "right":
        print(" " * (size - len(text)) + text)
aligntext()
