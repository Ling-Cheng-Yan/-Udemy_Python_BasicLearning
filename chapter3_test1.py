'''
小練習: 攝氏(C)轉換成華氏之程式，input為輸入攝氏溫度，output為印出華氏溫度。
公式: F = C * (9/5) + 32
'''
C = input('input your C: ')
C = float(C)
F = C * (9 / 5) + 32 #數學有先乘除後加減問題。
print('F is ', F)

