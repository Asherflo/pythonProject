number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

sum = number1 + number2 + number3
average = sum / 3
product = number1 * number2 * number3

print('the sum of first,second and third number is:', sum)
print('the average of first,second and third number is:', average)
print('the product first,second and third number is:', product)

smallest_value = number1
if smallest_value < number2:
    print('the smallest number is: ', smallest_value)
elif smallest_value < number3:
    print("the smallest value is : ", smallest_value)


max(number1, number2, number3)

# largest_value = number1
# if largest_value < number2:
#     print('the largest number is: ', largest_value)
# elif largest_value < number3:
#     print("the largest value is : ", largest_value)

