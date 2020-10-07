''' 
import(載入，裝別人寫好的功能進我們的程式)(可當成工具箱或一本書)
import時你要先下載你想import的檔案(模組)，才能import進來。random不用下載是因為python本身已經有了，在他的library裡(可當成圖書館)。
專業術語: module(模組)是一個檔案，package(套件)就是有多個module裝在一起(資料夾)
import時可以載入整個package或module。
想要有import是因為想要讓你的程式輕一點。
'''
import random  
r = random.randint(1, 100) #點可以翻譯成'的'，即random這工具箱的randint。randint即random int，即從哪到哪邊，產生隨機值。以此為例為從1~100產生一隨機值。
print(r)


'''
List(清單)(可想像成火車，火車有車廂編號，車廂內有人)
以前我們在講Data Types
資料型別有四種
整數 浮點數
布林值 字串
現在我們介紹第五種
叫做list 清單
那既然它都已經叫清單的
它就是用來裝東西的
清單的符號是中括號
可以混裝不同資料型別
index索引(代號)是從0開始(可想像0號車廂)
可用 .append()來加東西進入清單
用len()來取長度
用in來檢查東西在不在裡面
'''
a = [] #空清單
a = [True, 'Toyota', 'Honda', 1123]
print(a)
print(a[0], a[1], a[3])
a.append('Audi') #會加在最後面
print(a[4])
print(len(a))
print('Audi' in a) #是非題，return值只有True/False，in的後面一定要是清單(list)


'''
for loop
for loop就是把清單中的東西一個一個拿出來
for loop的第一個叫做暫時的變數。也就是說用在for loop，在for loop外就不會使用。
'''
cars = ['Toyota', 'Honda']

for car in cars:
	print(car)


'''
for loop
字串也可以當作清單，可以把字串每一個字母當作一個東西用for loop印出來。
所以字串也可以用in,len()，但不能用append。
'''
car = 'Audi' # ['A', 'u', 'd', 'i']

for c in car:
	print(c)
print('A' in car)
print('Au' in car)
print('x' in car)


'''
讀取檔案
下面的code印出來會中間多一行，是因為在檔案內我們有按到enter去換行，所以其實有存到一個換行符號，也就是"倒斜線n"。然後print會幫你換行，所以pasta換行，然後又讀到倒斜線n又換行。
'''
data = [] #想要看清單裝啥
with open('chapter4_read.txt', 'r') as f:  # r是讀取模式的意思，寫入模式是w。 as f就是當作是file的意思，意思就是把這個food.txt當作是f，因此從此以後只要需要用到這檔案，就只要打f就好。
	for line in f:    #line一樣在這邊是暫時取的變數，檔案會一行一行被讀取，每一行取名叫做line
		print(line)
		data.append(line)
print(data) #會發現pasta多一個倒斜線n，ramen沒有是因為那時候沒有按enter。

data = []
with open('chapter4_read.txt', 'r') as f:
	for line in f:
		data.append(line.strip()) #strip就是專門給字串用的，他會把換行或多餘的空格給去掉。append是專門給清單用的，所以兩者不能互用。
print(data)
#補充: with是自動關閉檔案的功能，以前沒with的時候，你開檔案都要自己手動關閉，現在有with就不用了。with那一block結束後就會自動關閉。


'''
range 範圍
python內鍵功能:清單產生器
range通常都跟for loop搭配，不會單獨寫出來。
'''
range(5) # [0, 1, 2, 3, 4] 自動從0開始，結尾值不包含
for i in range(5):
	print(i)

#for i in range真正的應用如下，只是為了讓它的內容重複執行某個固定次數!
for i in range(5):
	print('hi')
for i in range(10):
	r = random.randint(1, 100)
	print('這是第', i + 1, '次產生隨機數: ', r)


'''
range 延伸(但這種很少很少用，知道就好)
'''
range(2, 5) #[2, 3, 4]
range(2, 10, 3) #[2, 5, 8]
range(10, 3, -2) #[10, 8, 6, 4]



#補充: 要用for loop 還是 while loop通常關鍵在執行次數，若你不知道你想執行幾次就先用while True。