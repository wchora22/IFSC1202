str=input("Enter a string: ")
count=0
if len(str)>0:
    count=1
    for ch in str:
        if ch == ' ':
            count += 1
print(count, "words")