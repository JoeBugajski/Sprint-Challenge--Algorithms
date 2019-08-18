def bunnyEars(bunnies):
    print(bunnies)
    if bunnies == 0:
        return 0
    return 2 + bunnyEars(bunnies-1)

bunnyEars(8)