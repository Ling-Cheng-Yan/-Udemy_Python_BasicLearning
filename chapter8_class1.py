'''
class 類別是什麼
python中所有東西都是物件，他們都有class，差別在於有些是python本身已寫好的，像是int和string。有些你可以自己創造。
x = 5 是物件，它的class為int。
物件也有屬性，你可以打dir(x)去查屬性。

'''


'''
如何寫class
class寫法:
class <class名稱>:
	def __init__(self):
		.....
	def <其他function>(self):
		.....
'''
class Students: #字首大寫，前面有講過，小寫通常是function
	def __init__(self): #initialize 初始化之意，通常class都會先寫這個，把class初始設定都先做好。這是python內有的function，不是你自己創造的。只要這個class生出來或說創造時(被做成物件，或是直接使用)都會自動執行__init__()。
		print('我誕生了')

	def do_hw(self):
		print('我在做作業')

	def study(self):
		print('我在讀書')

print('執行 : s = Students()')
s = Students() #創造出物件，名為s，類別是students，

print('執行 : s.do_hw()')
s.do_hw() #使用class的do_hw()。注意這邊不會執行__init__()，因為這是創造時才會執行。

print('執行 : Students().do_hw()')
Students().do_hw() #也可以用這方式來執行，只是這個和33行比起來的缺點就是，它沒有被存下來，所以每次呼叫他都會重新創造一個，所以__init__()都會重新被執行。

print('執行 : s.study()')
s.study()
print('---------')

#補充: function是用來收納程式碼的, class可以想成收納function的。


'''
self是什麼:
class內的每個function你都可以透過self去共用
想像成一個房子，每間房間你都可以透過鑰匙(self)去開並拿裡面的所有東西。
功能:
	1. 使用self來存取自身上的function，而且self這個參數你不用去投它，python會幫你投。
	2. 使用self來增加身上的屬性(非function的屬性)。
	3. 典型的初始化參數設計。
	4. 用同一個class來創作不同的物件。
'''


'''
使用self來增加身上的屬性，包括function和非function。
'''
class Students:
	def __init__(self):
		print('我誕生了')
		self.name = 'Allen' #增加身上的屬性。此非function的屬性，要注意屬性要有等號去設值才會創作出來，不能只寫self.name 這樣會當掉。
		self.do_hw('英文')
		self.study()

	def do_hw(self, hw):
		print('我在做作業', hw)

	def study(self):
		print('我在讀書')

s = Students()
print(dir(s)) #可以看到有個屬性叫做name
print('------')
print(s.name) 
print('------')


'''
將self.name變成為一個浮動屬性。即典型的初始化參數設計。
'''
class Students:
	def __init__(self, n):
		print('我誕生了')
		self.name = n 
		self.do_hw('英文')
		self.study()

	def do_hw(self, hw):
		print('我在做作業', hw)

	def study(self):
		print('我在讀書')

s1 = Students('John') #將Allen投到__init__()的n參數。為啥不會投到do_hw()的hw參數? 因為這邊是在創造出物件s，創造只會執行__init__()，所以當然是投在這個function。
s2 = Students('Peter')
print(s1.name, s2.name)
print('------')

#補充: 通常我們會把n這個名稱取的跟你的屬性名字一樣，也就是self.name = name，但他們對應的參數位置和意義不一樣，別搞混。


'''
用同一個class來創造出不同的物件
'''
class Students:
	def __init__(self, name, score):
		print('我誕生了')
		self.name = name
		self.score = score

	def do_hw(self, hw):
		print('我在做作業', hw)

	def study(self):
		print('我在讀書')
		self.score += 5 #它可以自己去__init__()去找出這個屬性，並且去做運算。

s1 = Students('John', 100)
s2 = Students('Peter', 95)
print(s1.name, s1.score)
print(s2.name, s2.score)
print('------')

s2.study() #會執行self.score那行，因為你呼叫了這個function。
print(s2.name, s2.score)
print('------')


'''
class的應用
'''
students = [s1, s2] #等同一個清單裝成兩個字典
for s in students:
	print(s.name, '的分數是', s.score)


'''
寫class的三大好處:
1. 把相關function收納在一起 : 可做最大層級的收納。
2. 透過self來共用身上的屬性 : 當有許多function需用到同樣的參數時，可以透過self去共用。
3. 包裝程式碼 方便使用 : import時，可以很方便使用這些工具。
'''