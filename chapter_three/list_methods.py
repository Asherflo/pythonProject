prof = dict(name='segun',age=12)
print(prof)

lst =['segun','sege','oko','mama','e']
lst.append('kurubente')
print(lst)

lst.append(['kurubente', 'koga', 'fish'])
print(lst)

lst.extend(['kurubente', 'koga', 'fish'])
print(lst)

fruits = ['apple', 'grape','pear']
fruits.append('orange')
print(fruits)
fruits.extend('orange')
print(fruits)

fruits.extend(('orange', 'stone'))
fruits.append(('orange', 'stone'))
fruits.insert(1, 'pineapple')
fruits.insert(-1, 'pineapple')
fruits.insert(len(fruits), "bananna")
fruits.append("bananna")
print(fruits.pop(1))

# fruits.reverse('apple')
# fruits.('apple')
print(fruits)

