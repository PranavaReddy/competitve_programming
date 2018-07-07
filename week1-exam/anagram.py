# s2=string2.split()
# str1=""
# str2=""
# for i in range(len(string1)):
# 	if(i is None):
# 		continue
# 	else:
# 		str1=str1+string1[i]
# for i in range(len(string2)):
# 	if(i is None):
# 		continue
# 	else:
# 		str2=str2+string2[i]
def my_anagram(str1,str2):
	l1=[]
	l2=[]
	str1=str1.lower()
	str2=str2.lower()
	for i in str1:
		if(i!=' '):
			l1.append(i)
	for i in str2:
		if(i!=' '):
			l2.append(i)
	l1.sort()
	l2.sort()
	
	if(l1==l2):
		return True
	else:
		return False
s1=input()
s2=input()
k=my_anagram(s1,s2)
print(k)


