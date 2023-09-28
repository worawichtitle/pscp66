"""Blackjack"""
def main():
    """score >= 21"""
    draw = int(input())
    find_a = ""
    score = 0
    for _ in range(draw):
        card = str(input()).upper()
        find_a += card
        if card in ("J", "Q", "K"):
            score += 10
        elif card == "A":
            if score + 11 <= 21:
                score += 11
            else:
                score += 1
        else:
            score += int(card)
        if score > 21 and find_a.count("A") != 0:
            score -= 10
    print(score)
main()
