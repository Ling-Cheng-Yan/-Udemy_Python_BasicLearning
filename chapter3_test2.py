'''
練習: BMI計算程式
'''
height = input('input your height(cm): ')
weight = input('input your weight(kg): ')
height = int(height)
height = height / 100
weight = int(weight)
BMI = weight / (height * height)
print(BMI)
if BMI < 18.5:
	print('體重過輕')
elif 18.5 <= BMI and BMI < 24:
	print('正常範圍')
elif 24 <= BMI and BMI < 27:
	print('過重')
elif 27 <= BMI and BMI < 30:
	print('輕度肥胖')
elif 30 <= BMI and BMI < 35:
	print('中度肥胖')
else:
	print('重度肥胖')
