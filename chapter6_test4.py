'''
1. 分析留言最常出現的字
2. 一些import的函式庫功能
3. PYPI是套件大本營，使用前必須先看說明書才會使用
4. 在cmd用 pip install 套件名稱，此方式可用來安裝目前不在標準函式庫的功能
'''

import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000) #知道物件概念後，就可知，bar是個物件，他的型別是ProgressBar(這是全新發明的型別)。注意ProgressBar(max_value=1000000)是一個型別，不是function，因為如果是function那第一個字一定是小寫的，例如print()。
with open('chapter4_reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		bar.update(count) #因為bar是型別ProgressBar的物件，所以可以這樣用。
print('檔案讀取完畢，總共有', len(data), '筆資料')


#文字計數
start_time = time.time() #想知道這段code跑多久，單位是秒。
wc = {} #宣告空字典，word_count
for d in data: #d是第一筆留言，他是字串, data是清單
	words = d.split(' ') #split若()內都不寫，就預設是用空字串，且他遇到連續的空白時，他會當作沒看到直接跳過，不過去切。
	for word in words:
		if word in wc:
			wc[word] += 1 
		else:
			wc[word] = 1 #新增新的key進wc字典

for word in wc: #把字典的key給叫出來，注意不是value
	if wc[word] > 1000000: #把次數超過1000000的print出來
		print(word, wc[word])
end_time = time.time()
print('花了',end_time - start_time, 'seconds')

print(len(wc)) #可以知道字典有幾個key


#來讓使用者查詢字
while True:
	word = input('請問你想查甚麼字(q來終止): ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為', wc[word])
	else:
		print('沒有這個字喔')

