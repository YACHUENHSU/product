import os #operating system 用來確認檔案是不是存在

#讀取檔案
products = []
if os.path.isfile('products.csv'): #isfile是一個功能 確認在不在
	print('在唷在這裡, 找到檔案囉！')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #有點像break 但不會讓整個程式整個跳開
			name, price = line.strip().split(',') #原先 name = s[0] & price = s[1]
			products.append([name, price])
		print(products)
else:
	print('登愣 居然不在QQ')


#讓使用者輸入
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

#印出所有購買記錄
for product in products:
	print(product[0],'的價格是', product[1])


#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: #'w' write 寫入 #open打開檔案 #encoding 為編碼 #utf-8 讓文字不要亂碼
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ','+ p[1] + '\n')  #\n 是換行的意思



