numbers = int(input(" input a number"))
while numbers != 1:
    print(numbers)
    if numbers % 2 != 0:
        numbers = numbers * 3 + 1
    elif numbers % 2 == 0:
        numbers = numbers // 2
else:
    print(numbers)

