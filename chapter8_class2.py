'''
class總複習:
1. class名字第一個字要大寫
2. class裡的function(method)沒有順序的差別，沒有說__init__()一定要放在第一個，而且也可以還未先def就直接用self去使用這function。因為程式會直接先看過整個一遍再去執行class。
3. self.增加屬性不一定要在init裡，但是不這樣寫，不太好。因為想要創造出來時，就把非function的屬性都設定好。
4. class裡的function叫做method
5. method間隔一行, 而function間隔兩行
6. __init__()不一定要寫，但不寫的方法比較進階，這裡不講。
7. 繼承也是進階功能，這裡不講。
'''

class Player:
	def __init__(self, name, ap):
		print('我誕生了')
		self.name = name
		self.hp = 100
		self.ap = ap

	def attack(self, target):
		print(self.name, 'attacking', target.name)
		target.hp = target.hp - self.ap


p1 = Player('Player1', 5)
p2 = Player('Player2', 10)
p1.attack(p2) #若這邊引數改成5會當掉，因為5.name，沒辦法找到這東西。錯誤訊息會顯示，整數5沒有name這屬性。
print(p2.hp)


'''
另一個應用範例
'''
class Db:
	def __init__(self):
		self.connect()

	def connect(self):
		print('建立連線')

	def insert_data(self):
		print('abc')



class Tool:
	def __init__(self):
		print('sadasdasda')
		self.db = Db()

	def gggg(self):
		self.db.insert_data()  #一個物件連到另一個物件的method