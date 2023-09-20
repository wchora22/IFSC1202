value = input("Enter a number (CR to quit): ")
if value != "":
    maximum = int(value)
    maximumindex = 1
    currentindex = 1
    while value != "":
        if int(value) > maximum:
            maximum = int(value)
            maximumindex= currentindex
            currentindex += 1
    print("Maximum: {}".format(maximum))
    print("Index of maximum:{}".format(maximumindex))
else:
    print("Sequnece length is 0")