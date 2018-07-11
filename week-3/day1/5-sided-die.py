import random
def rand7():
    return random.randint(1, 7)
def rand5():
	while True:
        temp = rand7()
        if temp < 6:
            return temp
print 'Rolling 5-sided die...'
print rand5()