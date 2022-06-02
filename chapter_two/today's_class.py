#


# lst= []
# for i in range(65,94):
#     lst.append(chr(i))
# print(lst)
#
# add = lambda x,y: x +y
# print(add.__name__)


# def add(a, b):
#     return a + b
#
#
# def sub(c, d):
#     return d - c
#
#
# def muitply(a, b):
#     return a * b
#
#
# def operate(x, y, func):
#     return func(x, y)
#
#
# val_sub = operate(5, 24, sub)
# val_add = operate(5, 24, add)
# val_mutiply = operate(5, 24, lambda x, y: x * y)
# div = operate(4, 8, lambda x, y: y // x)
#
# print(val_sub)
# print(val_add)
# print(val_mutiply)
# print(div)
#
#
# def mutiples(x, funct):
#     return funct(x)
#
#
# def operate(x, funct):
#     return funct(x)
#
#
# print(mutiples(5, lambda x: (2 * x)))
# print(mutiples(5, lambda x: (x * x)))
# print(mutiples(5, lambda x: (8 ** x)))
#
#
#
#
# names = ["Amaka","Amanda" ,"Segun" , "Samson","Foil", "comb"]
# print(all([name.istitle() for name in names]))

# peoples =[
#         {"name":"Omosetan omolere", "age":30 ,"year_of_experience": 4, "langauage":["java", "python"]},
#         {"name":"Adeayomi florence", "age":28 ,"year of experience": 14, "langauage":["kotlin", "python"]},
#         {"name":"Amaka stephen", "age":22 ,"year of experience": 9, "langauage":["java","go", "python"]},
#         {"name":"Earnest adeole", "age":33 ,"year of experience": 15, "langauage":["java", "python","go"]}
# ]
#
#
# print([people["age"] <= 20 and "python" in people["langauage"]for people in peoples])
# print(any([people["age"] <= 28 and "python" in people["langauage"] for people in peoples]))
# print([people["name"] for people in peoples if people["age"] > 28 and "python" in people["langauage"]])


map_object = map(lambda x:x**2 if x % 2 == 0 else x,range(1,10))
lst1 =list(map_object)
lst2 =list(map_object)
print('1', lst1)
print('2', lst2)

def isEven(x):
    return x % 2== 0
filter_obj =list(filter(isEven,range(1,10)))
print(filter_obj)


from functools import reduce
fruits=["Apple","pear", "pineapples","watermelon","banana","cucumber"]
longest = reduce(lambda x,y: x if len(x) >= len(y) else y,fruits)
smallest = reduce(lambda x,y: x if len(x) < len(y) else y,fruits)
print(longest)
print(smallest)
print(max(fruits))
