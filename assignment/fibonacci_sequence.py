numbers = int(input("ENTER THE NUMBER OF THROW"))
number1, number2 = 0, 1
counter = 0


if numbers <= 0:
    print(" enter a number")
elif numbers == 1:
    print('fibonacci sequence is', numbers, ':')
    print(number1)
else:
    print('the fibonacci sequence are:')
    while counter < numbers:
        print(number1)
        total = number1 + number2
        number1 = number2
        number2 = total
        counter += 1
