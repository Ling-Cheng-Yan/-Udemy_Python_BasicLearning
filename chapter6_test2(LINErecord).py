'''
1. 聊天紀錄統計(LINE對話紀錄)，統計傳幾張圖片，誰講多少個字，圖片傳幾個。
2. 清單的切割寫法:
	n[開始值:結束值] (開始有包含，結束不包含)
	e.q. n[:3] 可以拿到前三個，index是0,1,2的都會拿到
	e.q. n[-2:] 可以拿到最後兩個，結尾不寫表示到底，另外數字是負的就代表從結尾開始數而已
'''


def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f: #需要utf-8-sig是因為只要是word或txt都有可能會有個偷存的看不到資料在第一行開頭，所以需要多個-sig就可以把第一行開頭那符號給去掉。
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines): #關鍵函式，遇到人名時，趕緊continue去取下一行，這樣下一行如果是句子就可以馬上附加上去。非人名表示都是那個人講出來的。
	person = None #關鍵，python特殊用法。可設person為無，雖然是無，但其實還是有個'值'，目的是為了跟24行做搭配。
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ') # split切割完會變成一個清單，一個清單內視切割物，有很多東西。
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('allen said' , allen_word_count, 'words.', 'send', allen_sticker_count, '貼圖', 'send', allen_image_count, '圖片')
	print('viki said', viki_word_count, 'words.' , 'send', viki_sticker_count, '貼圖', 'send', viki_image_count, '圖片')
		#print(s)


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('chapter6_LINErecord.txt')
	lines = convert(lines)
	#write_file('chapter6_FBoutput.txt', lines)

main()