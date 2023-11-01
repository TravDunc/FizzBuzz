i = 0
while i < 100:
    i += 1
    if i % 3 == 0:
        word = "Fizz"
    elif i % 5 == 0:
        word = "Buzz"
    else:
        word = ""
    print(i, word)
