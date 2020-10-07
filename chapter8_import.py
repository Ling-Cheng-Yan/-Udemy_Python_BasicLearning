'''
import
1. 可用,分開去一次載入很多個東西(可載function,class,變數)
2. from和直接import檔案的差別，直接import檔案的話，你如果要使用那個檔案的某個東西，你就要寫"檔案名.那個東西"，所以用from的話，就不用還要在打"點"了
3. from ... import * 。這個用法就是直接把那個檔案的所有東西都import進來。
4. 載入子資料夾裡的檔案(意思是往下層的資料夾去拿的話)。方式為 打個"點"。就像cd 會用/去切一樣，只是這邊用點去代表。
5. 載入母資料夾裡的檔案(python不允許你拿比較上層的檔案)，有方法可以解決，但是很進階，這裡不講。
'''
from chapter8_class2 import Db, Player
class Tool:
	def __init__(self):
		print('sadasdasda')
		self.db = Db()

	def gggg(self):
		self.db.insert_data()