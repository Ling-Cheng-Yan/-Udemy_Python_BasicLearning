'''
declare宣告就是創作，只有第一次遇到才會創作，若有遇到過，就只是改變內容而已。
x和y在此就是variable變數意思，5,1000,10,2就是value值的意思。
=等號即為設值assignment，即把右邊存到左邊。
'''
x = 5
print(x)
x = 10
x = 1000
y = 2
print(y)


'''
data types (種類)
資料型別
1. 整數  int
2. 浮點數(小數)  float
3. 布林值  bool (只有 True, False)
4. 字串  str (就是文字) 'Allen' (必須有一開一關，就是單引號或雙引號去框起來)
'''
price = 10 #int
pen = 0.38 #float
rain = True #boolean
name = 'Allen' #string
print(price)
print(pen)
print(rain)
print(name)


'''
print一次也可印很多個，記得用逗點分開就好，且這樣會印在同一行
'''
print(price, pen, rain, name)


'''
input(讓使用者輸入)，input不會讓程式結束，需等使用者輸入。把input放到name裡面存起來，並印出來。
'''
name = input('請輸入名字: ')
print('Hi', name) #印出一個單獨字串'hi'，以及一個變數name。


'''上傳到GitHub流程 :
1. 到GitHub新增專案(按new repository)
2. 桌面建新資料夾
3. cmd中cd進去新資料夾
4. 在cmd複製GitHub的那6行指令
4. 第一行 : 產生README檔，echo就是print，看你想print啥進去README。
5. 第二行 : 把資料夾初始化成git的資料夾(以後才可以在這資料夾做git指令)
6. 第三行 : 把README檔加入追蹤清單
7. 第四行 : 建立版本
8. 第五行 : 把資料夾跟雲端上的GitHub專案做連結
9. 第六行 : 上傳版本到雲端的GitHub專案
(此時就在GitHub上建立專案和README了，README就是說明書而已，接下來要看你想放啥py檔上去)
(六行指令中，最重要的是:
    git init (開始可用git指令)
    git add 檔名 (上傳想要的檔案)
    git commit -m "版本訊息" (設定版本)
    git push -u origin master (真正上傳GitHub的動作)(有沒有-u都沒差))
10. 把想放的py檔放到新資料夾
11. 上傳py檔案要執行以下 :
    (git指令三部曲)
    git add 檔名
    git commit -m "版本訊息"
    git push origin master
'''

