print("Enter two integers,and i will tell you the relationships they satisfy. ")
number1 = int(input("Enter first number: "))
number2 = int(input("Enter the second number: "))
if number1 == number2:
    print(number1, 'is equal to', number2)
if number1 != number2:
    print(number1, 'is not equal to', number2)
if number1 >= number2:
    print(number1,"number1 is greater than or equal to number")

minimum_value = number1
if minimum_value < number2:
    print('the minimum value is', minimum_value)
else:
    print(number2, 'the minimum value is the second value then')








