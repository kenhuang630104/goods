
import os

#讀取檔案
def read_file(filename):
    goods = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            goods.append([name, price])
    return goods


#輸入資料
def user_input(goods):
    while True:
        name = input('please input the product name:  or \'q\'for exit!!')
        if name == 'q':
            break
        price = input('please input the product price:')
        goods.append([name, price])
    print(goods)
    return goods
#print(goods[0][1])#第1個大清單中的第2個欄位


#列出紀錄
def print_goods(goods):
    for p in goods:
        print(p)
#	print(p[0], '的價格是', p[1])


#寫入檔案
def write_file(filename, goods):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('商品,價格 \n')
        for p in goods:
            f.write(p[0] + ',' + p[1] + '\n')
def main():
    filename = 'goods.csv'
    if os.path.isfile(filename):
        print('yeah!!found the file!!')
        goods = read_file(filename)
    else:
        print('not found!!')
    goods = user_input(goods)
    print_goods(goods)
    write_file('goods.csv', goods)


main()
