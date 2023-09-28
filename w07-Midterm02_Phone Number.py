"""Phone Number"""
def phone(number, country):
    """Print phone number for Doestic or International"""
    phone_number = ""
    lphone = len(number)
    for num in range(0, lphone):
        if num % 4 == 0 and num != 0:
            phone_number += " "
        if country == "International" and num == lphone - 1:
            phone_number += "66+"
        else:
            phone_number += number[num]
    print(phone_number[::-1])
phone(str(input())[::-1], str(input()).capitalize())
