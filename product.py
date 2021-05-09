products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = [] #小清單
	p.append(name) #append 加到小清單
	p.append(price)
	products.append(p) #其實可以直接寫成 p = [name, price] #更簡潔的方式為 products.append([name, price])
print(products)

products[0][0] #把第零的商品拿出來

for product in products:
	print(product[0],'的價格是', product[1])

