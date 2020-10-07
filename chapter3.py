'''
好的寫法
coding style 寫程式的'風格'
x = 5 (O)
x=5 (X)
print('hi', x) (O)
print('hi',x) (X)
變數的命名:
    命名建議要貼切和直覺，不要只有x,y,z這樣。命名也幾乎都小寫開頭。
    另外，若命名有好幾個單字的，可用，例如:my_name，而不是myname。
    命名開頭不要也不要數字開頭。
    python的預留字不能當變數名稱，例如:if,lambda,try等等很多......。
'''


'''
註解放在上面的話，用來解釋後面那一段的code，註解放在一行code的右邊
的話，就是解釋那一行而已。，註解可以用三個引號的多行註解，或用#的單
行註解。
'''


'''
比較符號，想像成在問一個是非題，return值一定是布林值:True或False
'''
x = 5 
print(x == 5) #是否等於
print(x != 5) #是否不等於
print(x > 2) #是否大於
print(x < 2) #是否小於
print(x >= 2) #是否大於等於
print(x <= 2) #是否小於等於


''' 
if 架構，if後面一定要是個會算成布林值:True/False的問題，然後一定要記得有冒號(可以想像冒號是如果有....的話)。
'''
rain = input('Rain today? ')
if rain == 'yes':  # if如果值是True就會進入下面的block，否則不進block，另外python的block以空格為區分。
	print('umbrella')
	print('eating')


'''
什麼是區塊(block)?
python是以block來區分程式碼的執行，類似C/C++的{}，開頭的判斷式判斷要不要進去block裡面。只要是空格數相同的程式碼就叫做同一個block，空格的話都是4個空格或1個tab為單位。
block用意是要知道code是在裡面還是外面，執行結果可能會因此而差很多，像是會有明明if條件沒過不會執行if內的block的print，但因你print寫在if的block外面，他就會去執行。
下面code有雙重if，第二個if裡面的print就是和第一個if是不同block的，因為空格數不同。看block的時候可以圈起來去看，像55~58是54(開頭不用圈進去)的一個block，58是57(開頭)的一個block。
另外，你可以用tab或四個空白鍵去空格，但不能混著用，而subline的幫你自動換行是用tab。
你可以ctrl+a全選去看到底是空格鍵還是用tab，一條線就是tab，有點點的就是空白鍵。
另外，google公布的寫法指南是用空白鍵去空格。
'''
rain = input('Rain today? ')
if rain == 'yes': 
	print('umbrella')
	print('eating')
	if x > 3:
		print('right!')


'''
型別轉換(Casting)。
比較判斷符號不能把字串和整數做比較，所以下方的code會錯誤，因此需要型別轉換。
重點補充: input()永遠都會存成字串，所以就算你輸入的是數值，也會是字串的30。

age = input('your age: ')
if age >= 20: 
	print('you can vote.')
'''
age = input('your age: ')
age = int(age) #Casting
if age >= 20:
	print('you can vote.')


'''
如何更改README:
	用subline在資料夾中開出README檔案，#在README是大標題的意思。
	打完後儲存，然後一樣使用Git指令三部曲:
		git add README.md
		git commit -m "Update README"
		git push origin master
'''


'''
else(if架構延伸)，延伸指的是他們都是同一個block，也就是if和else只會執行一個。
'''
age = input('your age: ')
age = int(age)
if age >= 20:
	print('you can vote.')
else:
	print("you can't vote!")


'''
elif(if架構延伸)，elif和else都只是if的延伸，整個是1個if的架構，也就是說他們都必須要接在if底下才行。還有else一定是放在if架構的最後面，他捕捉所有剩下的可能性。if後面可以接無限個elif和只有一個else。
下面code兵分四路，下面code有四個block，然後只會有一路進去print。
注意!!雖然有四個block，但整個都是if的一個架構，所以if和elif和else只會執行一個。
'''
age = input('your age: ')
age = int(age)
if age < 13:
	print('國小')
elif age >=13 and age < 18: #and就是把兩個問題串接在一起，要兩個問題都符合才會進去block。還有'or'就是其中一個問題符合即可。
	print('國高中')
elif age >= 18 and age < 22:
	print('大學')
else :
	print('社會')	


'''
良好的專案開發模式，為:
	1. 先建立GitHub專案(一樣要複製那六行code)
	2. 開始在subline寫py檔
	3. 用Git指令三部曲來新增py檔
	4. 當需要更新檔案的時候，一樣用Git指令三部曲去更新，檔名不用變，版本部分改變就好了，來提示自己做了啥更改。
'''


'''
while 有限迴圈(跑操場，每跑完一次就問教官可不可以不要跑了)
'''
x = 5
while x < 10:
	print('x小於10喔!') #一直重複做這段話，只要x一直小於10。即條件false才會跳出去迴圈。
	x = x + 1 #表示會印5次。(5,6,7,8,9都會做print)


'''
while 無限迴圈，當程式在執行無限迴圈想終止時，可按Ctrl+c
'''
while True:
	mode = input('請輸入遊戲模式: ')
	if mode == 'q':
		break #無限迴圈要逃離迴圈的話，要用break來逃離迴圈。
	elif mode == '1':
		print('mode 1')
	elif mode == '2':
		print('mode 2')
	else:
		print('only 1 or 2 or q')


'''
time.sleep()
用來暫停程式碼執行，單位是秒，例如time.sleep(1)就是暫停1秒。
使用時要先import time。time是python本身有的模組。
'''


