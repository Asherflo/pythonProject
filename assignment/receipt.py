products_ = []
quantity_ = []
price_ = []
total_ = []


count = 0
state =True
while state:
    product = str(input("enter your product name:"))
    products_.append(product)

    quantity = int(input("enter the quantity"))
    quantity_.append(quantity)

    price = int(input("enter the price"))
    price_.append(price)

    total = price * quantity
    total_.append(total)

    count += 1
    print('do you want to buy more')
    answer= int(input("""enter
                            1-->yes
                            2 --no"""))
    print()
    print()
    print()
    print()


    if answer == 1:
        state = True
    elif answer == 2:
        state = False

final_total = sum(total_)
print()
print()
print()
print()
print()


star ="*"
print(star * 40)
print("Florence & Sons group of company \n312,Herbert Macurlay,sabo-yabo\n070144014017,florenceandsons@gmail.com")
print("                                      product   quantity    price  total")
for i in range(0, count):
    print(f'{products_[i]:>23}    {quantity_[i]:>12}  {price_[i]: >6}  {total_[i]:>9}')
print(star * 40)
print("  "*16 + "the total is:     ", final_total)
print(                                 star * 40)


















