"""BigFrame"""
def bigframe():
    """Put the text in the frame"""
    text1 = str(input()).strip()
    text2 = str(input()).strip()
    text3 = str(input()).strip()
    text4 = str(input()).strip()
    text5 = str(input()).strip()
    frame = long(text1, text2, text3, text4, text5)
    print("*" * (frame + 4))
    print("* " + text1 + " " * (frame - len(text1)) + " *")
    print("* " + text2 + " " * (frame - len(text2)) + " *")
    print("* " + text3 + " " * (frame - len(text3)) + " *")
    print("* " + text4 + " " * (frame - len(text4)) + " *")
    print("* " + text5 + " " * (frame - len(text5)) + " *")
    print("*" * (frame + 4))

def long(text1, text2, text3, text4, text5):
    """Find longest len"""
    return max(len(text1), len(text2), len(text3), len(text4), len(text5))
bigframe()
