def counting_bits(li):
	l2=[]
	length=len(li)
	for i in li:
		i=str(i)
		# print(i)
		l=len(i)
		count=0
		# print(i,"iiii")
		for j in i:
			# print("second loop")
			# print(j,"jjjjj")
			if(j=='1'):
				# print("hello")
				count=count+1
				# print(count,"count")
		l2.append(count)
	print(l2)
def convert_to_binary(n):
	li=[]
	li.append(0)
	for i in range(1,n+1):
		x=i
		temp=""
		while(x>0):
			r=x%2
			temp=str(r)+temp
			x=x//2
		# print(temp)
		li.append(temp)
	counting_bits(li)


n=int(input())
convert_to_binary(n)