'''
猜數字遊戲 :
讓使用者決定產生隨機數字範圍
讓使用者重複輸入數字去猜
猜對就印出"終於猜對了!"
猜錯的話，要告訴他，比答案大/小
要印出猜了幾次
'''
import random
start = input('請決定開始值: ')
end = input('請決定範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1
	answer = input('guess your number: ')
	answer = int(answer)
	if answer == r:
		print('終於猜對了!')
		print('這是你猜的第', count, '次!')
		break
	elif answer > r:
		print('比答案大')
	elif answer < r:
		print('比答案小')
	print('這是你猜的第', count, '次!')

