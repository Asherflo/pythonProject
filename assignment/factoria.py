number = int(input("enter a non-negative value: "))
counter = 1
for i in range(1, number + 1):
    counter = counter * i
    print("the factorial of ", number, "is: ", counter)
