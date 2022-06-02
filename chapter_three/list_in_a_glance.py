# list constructor
lst = list("adcdefghijklnmop")
print(''.join(lst))
print(lst[5])

lst = list("adcdefghijklnmop")
print(lst[1:5])
print(lst[::-1])
print(lst * 2)
print(lst +[1,2,3])
lst += [1,2,3,4,5]
print(lst)
print('a' in lst)
print('q' not in lst)

product = ['maggi', 'salt', 'rice']
price = [800, 79, 500]
for i, product in enumerate(product):
    # for j, price in enumerate(price):
    print(f'{i}: {product}')

product = ['maggi', 'salt', 'rice']
price = [800, 79, 500]
for i, product in enumerate(product):
    for j, price in enumerate(price):
        print(f'{i}:{product}')
        print(f'{j}:{price}')
