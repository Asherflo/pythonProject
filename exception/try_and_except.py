def divide(a ,b):
    if b == 0:
         raise ValueError("Denominator can nit be zero")
    return a / b
# # #print(divide(1,2))
# # #print(divide(2,1))
# # #print(divide(2,0))
# # try:
# #     print(divide(2,0))
# # except:
# #     print("wrong value")
#
#
#
#
#
#
# num = int(input("enter the numerator: "))
# den = int(input("enter the numerator: "))
#
#
#
# while True:
#     try:
#         print(divide(num,den))
#         break
#     except:
#         print("Wrong value")
#         num = int(input("enter the numerator: "))
#         den = int(input("enter the numerator: "))

try:
    print("life's good")
    # print(1/0)
    print([1,2,3][4])
    print("after life")
except ZeroDivisionError as e:
    print ("ZeroError",e)
except IndexError as e:
    print("IndexError", e)
else:
    print("else,i run only when there is no error")
finally:
    print("finally , i run every time")