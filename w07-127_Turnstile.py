"""Turnstile"""
def spin():
    """put Coin first then Push"""
    get_in = 0
    frist = ""
    action = ""
    while True:
        word = str(input()).upper()
        if word == "END":
            break
        action += word
    for char in action:
        if frist == "C" and char == "P":
            get_in += 1
        frist = char
    print(get_in)
spin()
