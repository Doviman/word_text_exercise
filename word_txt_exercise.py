fin = open('words.txt')
# print only the words with more than 20 characters (not counting whitespace).
for line in fin:
	word = line.strip()
	if len(word) > 20:
		print (word)
