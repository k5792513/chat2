
def read_file(filename):
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		lines = []
		for line in f:
			lines.append(line.strip())
		return lines

def convert(lines):
	person = None
	Allen_word_count = 0
	Allen_sticker_count = 0
	Allen_photo_count = 0
	Viki_word_count = 0
	Viki_sticker_count = 0
	Viki_photo_count = 0
	for line in lines:
		s = line.split(' ')
		name = s[1]
		time = s[0]
		if name == 'Allen':
			if s[2] == '貼圖':
				Allen_sticker_count += 1
			elif s[2] == '圖片':
				Allen_photo_count += 1
			else:
				for m in s[2:]:
					Allen_word_count += len(m)
		if name == 'Viki':
			if s[2] == '貼圖':
				Viki_sticker_count += 1
			elif s[2] == '圖片':
				Viki_photo_count += 1
			else:
				for m in s[2:]:
					Viki_word_count += len(m)
	print('Allen說了', Allen_word_count, '字、傳了', Allen_sticker_count, '個貼圖及', Allen_photo_count, '張圖片')
	print('Viki說了', Viki_word_count, '字、傳了', Viki_sticker_count, '個貼圖及', Viki_photo_count, '張圖片')






		#print(s)
	


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	print(lines)
	lines = convert(lines)
	#write_file('output.txt', lines)

main()


