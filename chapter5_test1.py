'''
練習寫入檔案
'''
data = [1, 3, 5, 7, 9] # 清單中裝著一些整數

# 請開始寫"寫入檔案"的程式碼
with open('chapter5_test1(data).txt', 'w') as f:
	for d in data:
		d = str(d)
		f.write(d)

#關鍵: d從list取出來是數值，不是字串，所以要先轉換才能用f.write()