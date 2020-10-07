'''
建立記帳程式專案(+二維清單)
二維清單，想像成大火車裡面的每節車廂還有小火車
'''
products = []
while True: 
	name = input('請輸入商品名稱(若需要結束請輸入q): ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = []
	p.append(name)
	p.append(price)
	products.append(p) #前面說過，append就是把任何東西都可以加入清單，注意字串也算清單，但他不能用。
print(products)

products[0][1] #大火車的第0格裡面小火車的第1格

#其實11~13行可以寫 p = [name, price]。

for p in products: #把小火車分別取出來。
	print(p)

for p in products: #把小火車的第0格取出來。
	print(p[0])


'''
寫入檔案
補充: 字串可以做加與乘
	加法: 'abc' + '123' = 'abc123' (很常用)
	乘法: 'abc' * 3 = 'abcabcabc' (沒很常用)
寫入欄位名稱+編碼問題
'''
with open('products.csv', 'w', encoding = 'utf-8') as f: #'w'和'r'差在'w'可以覆寫檔案或若本來無檔案會新增此檔案。
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') #f.write就是f這'w'檔案格式的功能，就是可以把()內的內容寫進去。

#補充: CSV檔案，會以逗號來做資料的區隔，所以若你少了逗號，那他會把p[0]和p[1]塞在同一格。
#補充: 把CSV檔案拉到subline不會出現亂碼，但直接打開excel會有是因為excel沒設定用utf-8編碼去開啟，所以你要去excel那邊設定。從excel的資料那邊設定，導入txt檔。然後設定就好。
#補充: utf-8是世界最有名的編碼方式，盡量都用這個。


'''
讀取檔案+split()
補充:讀取檔案都是一行一行去讀，寫的話不是，想一行一行寫要+換行符。
split()是字串用法，用來切割字串，切割點就看你想怎樣切，如果你想遇到','就切那就打split(',')。記住split完的東西會變成清單(list)。
'''
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f: #記得要加encoding，因為讀寫都有編碼問題。
	for line in f:
		s = line.strip().split(',') #這句話意思是，我們在line上面做了strip後，再做split這件事情(順序別搞錯)。而想要有strip就是因為想把換行符號給去掉，因為讀出來的時候會讀到。
		name = s[0]
		price = s[1]
		products.append([name, price]) #從products這list中，再建立一個list裡面有name和price。

print(products)
#補充: 53~55行可以寫 name, price = line.strip().split(',')。但要記得，你數量要一一對應，切成三塊，那你變數就要有三個去存。


'''
continue用法(跳過一次迴圈，跳到下一次迴圈)
記住，continue和break一樣都只能寫在迴圈裡面。
continue的使用時機通常都放在loop比較高的位置，因為這樣才有意義，才有東西跳過。
'''
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue #遇到continue後，直接執行下一次的loop，即70~73先不執行。
		s = line.strip().split(',') 
		name = s[0]
		price = s[1]
		products.append([name, price]) 

print(products)


'''
檢查檔案在不在
'''
import os #operating system
if os.path.isfile('products.csv'): #path是os的模組，isfile是path模組其中一個功能。如果只給檔名那就是相對路徑(就是預設目前的資料夾)，要絕對路徑的話要額外打。
	print('Yes!')
else:
	print('No.')


'''
function (函式)
function是用來收納程式碼的，它是個功能。
要執行function要先define才能執行。
寫程式時，盡量把程式碼都收納在function內，是良好的作法，這樣程式才清楚架構，而且有能重複使用的功能。
'''
def wash():
	print('加水')
	print('加洗衣精')

wash() #使用function


'''
function的parameter (參數)(想像成投幣孔)
1. 當function需要外部資料，我們就設計投幣孔(參數)，把資料投進function。
2. 如果function有投幣孔，你就一定要投東西。除非你有預設值。
3. 投東西的時候，自動是按照參數(孔)的順序
4. 參數可以有預設值，那就不一定要投它了。
5. 投東西給參數的時候，可以明確指定要投到哪個參數。
'''
def wash(dry):
	if dry:
		print('烘衣')

wash(True)

def add(x, y): #有兩個投幣孔一定要給兩個東西，你不能多給也不能少給。
	print(x + y)

add(3, 4)

def add(x=0, y=1): #預設值寫法。補充:寫參數的時候，等號左右不用空格。
	print(x + y)

add()#沒投東西就自動用預設值

def add(x=0, y=7):
	print(x + y)

add(5) #有投東西就照順序先給，所以先給x
add(y=5) #也可以指定要投給y


'''
function return 回傳
1. function如果有return，就可以把function執行的結果給存下來。可以想像成function運行完後會化身成為return的東西。
'''
def average(numbers): 
	avg = sum(numbers) / len(numbers) #sum()是list自動做加總的功能。
	return avg

a = average([1, 2, 3]) #引數可以用list
print(a)


'''
補充:
1. function可以有很多個return，但她遇到第一個return就會結束了。
2. function定義的時候記得要加冒號。
3. 以下程式碼不會印，因為python規定參數的部分，"沒預設值的"　一定要在　"有預設值的"　的前面，所以上面這個程式不行運作。
def hello(x=1, y):
    print(x, y)
 
hello(3, 4)
'''


'''
理想的function應該盡量只做一件事情，然後程式碼要有main()這個function當作程式的進入執行點比較好，就是C/C++的那種int main()。只不過python沒這東西，所以你可以定義，然後當作它就是C/C++的那種int main()。
所以main()裡面就是主程式，裡面可能call各種function這樣。記得，定義完main後，還是要記得main()去執行它。
'''

