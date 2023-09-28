"""Rectangle"""
def main():
    """Find area and perimeter"""
    high = int(input())
    wide = int(input())
    area = high * wide
    perimeter = (2 * high) + (2 * wide)
    print("%d \n%d" % (area, perimeter))
main()
