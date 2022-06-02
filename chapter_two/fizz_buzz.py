number = 1
while number < 101:

    if number % 15 == 0:
        print('fizz \nbuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)
    number +=1
else:
    print(number)
