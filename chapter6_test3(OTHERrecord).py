'''
1. 格式改寫
2. 清單的另一種格式:
	e.q. s[0][:5] (把s[0]那格的前5個東西給拿出來)
3. 為何 [:]方法是清單分割法，而此例中清單內是字串，怎也能分割?
	ans:因為前面說過字串也可以當成清單來看待。


'''

lines = []
with open('chapter6_OTHERrecord.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	print('name is', name)