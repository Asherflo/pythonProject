# generate list from 1 -
#
#
# lst =[num for num in range(1, 11)]
# even = [num for num in range(1 ,11) if num % 2 == 0]
# even_and_squared_odds = [num if num % 2 == 0 else num ** 2 for num in range(1, 11)]
# lst_input = [int(input("enter a number: ")) for num in range(1, 5)]
# list_nested_for =[(x, y) for x in range(1,5) for y in range (6,10)]
# upper_names = [len(name.title()) for name in ["dolapo", "tolani","florence"]]
# list_of_dict= [{key:value} for key,value in zip(upper_names,even)]
#
# print(lst)
# print(even)
# print(even_and_squared_odds)
# print(lst_input)
# print(list_nested_for)
# print(upper_names)
# print(list_of_dict)

# s1 = {1, 2, 3, 4, 5, 6, 7, 8}
# s2 = {3, 4, 5, 67}
# t = (s1.union(s2))  # union method
# t = (s1.difference(s2))  #different method
# t = (s1.__ior__(s2))
# t = (s1 > s2)
# print(t)

dict_play ={"name": "Tolani","age":32,"influenced":"samson"}
dict_play.items()               #to display alldict items
dict_play.keys()               #to display all keys only
dict_play.fromkeys("hello","unknown")               #to display all keys only
print(dict_play.fromkeys("hello","unknown"))
