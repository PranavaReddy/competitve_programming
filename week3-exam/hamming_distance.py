def hamming_distance(temp,flag):
	l1=len(temp)
	l2=len(flag)
	if(l2>l1):
		t=l2-l1
		while(t>0):
			temp="0"+temp
			t-=1
	else:
		t=l1-l2
		while(t>0):
			flag="0"+flag
			t-=1
	length=len(temp)
	count=0
	for i in range(length):
		if(temp[i]!=flag[i]):
			count=count+1
	print(count)

def convert_to_binary(x,y):
	# print("word")
	# print(x,y)
	temp=""
	flag=""
	while(x>0):
		r=x%2
		# print(r,"remainderrr")
		# print(x,"xxxxxxxxxxx")
		temp=str(r)+temp
		x=x//2
	# print(temp,"temppppp")
	while(y>0):
		d=y%2
		flag=str(d)+flag
		y=y//2
	# print(flag,"flagg")

	# print("hello")
	return hamming_distance(temp,flag)

x=int(input())
y=int(input())
convert_to_binary(x,y)