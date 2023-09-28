"""Elo"""
def main():
    """Find Ea Eb"""
    valra = int(input())
    valrb = int(input())
    want = str(input()).upper()
    if want == "A":
        score = 1 / (1 + 10 ** ((valrb-valra) / 400))
    else:
        score = 1 / (1 + 10 ** ((valra-valrb) / 400))
    print("%.2f" % score)
main()
