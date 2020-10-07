'''
聊天紀錄格式改寫，把chapter6_input檔改成像chapter6_output檔那樣
學習重點:
1. 寫良好的程式架構(有function和main function)
2. convert() 使用了continue來跳到下一行
3. None適合用來當預設值
'''


def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f: #需要utf-8-sig是因為只要是word或txt都有可能會有個偷存的看不到資料在第一行開頭，所以需要多個-sig就可以把第一行開頭那符號給去掉。
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines): #關鍵函式，遇到人名時，趕緊continue去取下一行，這樣下一行如果是句子就可以馬上附加上去。非人名表示都是那個人講出來的。
	new = []
	person = None #關鍵，python特殊用法。可設person為無，雖然是無，但其實還是有個'值'，目的是為了跟24行做搭配。
	for line in lines:
		if line == 'Allen':  
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: #需要這個if person是因為必須要第一行一定是人名，因為person會沒出現過就要用。
			new.append(person + ': ' + line)
	return new


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('chapter6_FBinput.txt')
	lines = convert(lines)
	write_file('chapter6_FBoutput.txt', lines)


main()