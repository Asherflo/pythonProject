class CustomList(list):
    def _getitem_(self, index):
        if index <= 0:
            raise IndexError("Index out of bounds")
        return super(CustomList, self).__getitem__(index - 1)

    def __setitem__(self, key, value):
        if key <= 0:
            raise IndexError("Index out of bounds")
        return super().__setitem__(key - 1,value)




l = CustomList()
l.append(2)
l.append(8)
l.append(9)
l.append(5)
l.append(2)
print(l._getitem_(4))
# print(l[0])
# print(l[1]==8)


