'''
留言分析程式
'''
data = []
count = 0
with open('chapter4_reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data)) #目的是希望只要是第1000筆資料就印出1000，表示現在進度是第1000筆資料
print('檔案讀取完畢，總共有', len(data), '筆資料')
print(data[0]) #可印出第一筆留言

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('留言平均長度是',sum_len / len(data)) #計算每筆留言的平均長度


#留言篩選，若你長度小於100，我才把你裝進清單內
new = []
for d in data:
	if len(d) < 100: 
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')


#另一個留言篩選範例。
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')


#清單快寫法，此方式完全等於上面那個篩選，但更簡潔。
'''
output = [(number-1) for number in reference if number % 2 == 0]
             運算          變數         清單      篩選條件
'''
good = [d for d in data if 'good' in d] #第一個d就是good.append(d)的意思

good = [1 for d in data if 'good' in d] #只要good有在你留言裡面，就把1給裝進去，而不是留言d。
print(good)

bad = ['bad' in d for d in data] #只要留言裡面有提到bad就印出True，由於我後面沒有篩選，所以會去看100萬筆留言。
print(bad)
#補充: 清單快寫法通常運算都放原封不動的那種，有放特別的都是做數據處理那種應用比較多。


'''
48~49等同如下
'''
bad = []
for d in data:
	bad.append('bad' in d)