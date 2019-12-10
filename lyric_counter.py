import re
def lyric_counter():
	try:
		local_file = open('lyric','r')
	except IOError:
		print "no file found"
	else:
		lyric_content = local_file.read()
		words = re.findall(r'\w+',lyric_content)
		word_list = []
		for i in words:
			word_list.append(i)

	word_set = list(set(word_list))

	word_freq = []
	for w in word_set:
		word_freq.append("0")


	for y in word_list:
		
		for x in range(int(len(word_set))):
			if y == word_set[x]:
				word_freq[x] = int(word_freq[x]) + 1
	#print word_freq
	#print word_set
	new_l = zip(word_freq,word_set)
	new_l.sort(reverse=True)
	for ii in range(10):
		print new_l[ii]

if __name__ == '__main__':
	lyric_counter()