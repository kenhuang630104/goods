import os


goods = []
if os.path.isfile('goods.csv'):
    print('yeah!!found the file!!')
    with open('goods.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            goods.append([name, price])
    print(goods)
else:
    print('not found!!')

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
#	print(p[0], '的價格是', p[1])

with open('goods.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格 \n')
	for p in goods:
		f.write(p[0] + ',' + p[1] + '\n')



