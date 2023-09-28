"""ProgressiveTax"""
def tax(salary):
    """You can't escape the TAXES"""
    paytax = 0
    while True:
        if salary <= 150000:
            break
        elif salary <= 300000:
            paytax += int((salary - 150000) * (5 / 100))
            salary -= salary - 150000
        elif salary <= 500000:
            paytax += int((salary - 300000) * (10 / 100))
            salary -= salary - 300000
        elif salary <= 750000:
            paytax += int((salary - 500000) * (15 / 100))
            salary -= salary - 500000
        elif salary <= 1000000:
            paytax += int((salary - 750000) * (20 / 100))
            salary -= salary - 750000
        elif salary <= 2000000:
            paytax += int((salary - 1000000) * (25 / 100))
            salary -= salary - 1000000
        elif salary <= 4000000:
            paytax += int((salary - 2000000) * (30 / 100))
            salary -= salary - 2000000
        elif salary > 4000000:
            paytax += int((salary - 4000000) * (35 / 100))
            salary -= salary - 4000000
    print(int(paytax))
tax(int(input()))
