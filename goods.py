goods = []
while True:
	name = input('please input the product name:  or \'q\'for exit!!')
	if name == 'q':
		break
	price = input('please input the product price:')
	goods.append([name, price])
print(goods)
#print(goods[0][1])#第1個大清單中的第2個欄位

for p in goods:
	print(p)
	print(p[0], '的價格是', p[1])


