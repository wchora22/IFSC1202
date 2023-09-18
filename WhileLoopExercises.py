sequencesum=0
sequencecount=0
value = int(input("Enter a number (CR to quit): "))
while value != '':
    sequencesum += int(value)
    sequencecount += 1
    value = input("Enter a number (CR to quit: )")
if sequencecount != 0:
    sequenceaverage= sequencesum/sequencecount
    print("Average: {}".format(sequenceaverage))
else:
    print("Sequence length to is 0")