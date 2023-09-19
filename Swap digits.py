n=int(input("Enter a number: "))
first_dig = n//10
second_dig = n%10
swapnum = (second_dig*10)+first_dig
print("Last digit: {}".format(swapnum))