'''
密碼重試程式:
先在程式碼中，設定密碼password = 'a123456'，讓使用者最多輸入3次密碼，不對的話，就印出"密碼錯誤!還有_次機會"，對的話就印出"登入成功!"
'''
password = 'a123456'
i = 3
while i > 0:
	user = input('請輸入使用者密碼: ')
	if user == password:
		print('登入成功!')
		break
	else:
		i = i - 1
		if i > 0:
			print('密碼錯誤! 還有', i, '次機會')
		else:
			print('沒機會嘗試了!')