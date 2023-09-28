"""Frame"""
def pic(text):
    """Put text in the frame of *"""
    frame = "*" * (len(text) + 2)
    print((frame + "\n*%s*\n" + frame) % text)
pic(input())
