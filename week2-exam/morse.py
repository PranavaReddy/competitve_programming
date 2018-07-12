def unique_morse_code(words):
	morse={"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.",
		"O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--.."}
	li=[]
	for i in range(len(words)):
		temp=""
		for j in range(len(words[i])):
				k=words[i][j].upper()
				# print(morse[k])
				temp=temp+morse[k]
				# print(temp)
		if temp not in li:
			li.append(temp)
	print(len(li))


words=[]
words=eval(input())
unique_morse_code(words)



