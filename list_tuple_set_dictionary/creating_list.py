c = [-45, "seyi", 89, 90.50, 1234]
print(c)
print(c[3])
print(len(c))
c[4] = 17
print(c)

a_list = []
for number in range(0,6):
    a_list += [number]
print(a_list)
def cube_list(value):
    for i in range(len(value)):
        value[i] **= 3
numbers = [1,2,3,4,5,6,7,8,9,10]
cube_list(numbers)
print(numbers)

