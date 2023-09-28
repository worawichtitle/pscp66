"""Virus I"""
def check_virus(virus):
    """Find body of virus"""
    body = 0
    for text in virus:
        if text == "o":
            body += 1
    print(body)
check_virus(input())
