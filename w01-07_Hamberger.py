"""Hamberger"""
def main():
    """MORE CARBOHYDRATES"""
    leftbun = int(input())
    rightbun = int(input())
    meat = "*" * ((leftbun + rightbun) * 2)
    burger = ("|" * leftbun) + meat + ("|" * rightbun)
    print(burger)
main()
