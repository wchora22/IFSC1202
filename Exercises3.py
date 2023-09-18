n = int(input("Enter number of cards: "))
sumallcards = 0
for i in range(1, n + 1):
    sumallcards += i
sumcards = 0
for i in range(n-1):
    sumcards += int(input("Enter card: "))
print (("Missing card: ").format(sumallcards - sumcards))