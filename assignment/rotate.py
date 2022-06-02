num=[0, 1, 2, 3, 4, 5, 6]
print(num[-3:] + num[:-3])


def rotate (lst,k):
    k = k% len()
    return lst[-k:] +lst[:-k]


list2 = list(range(1, 10))
print(list2)
