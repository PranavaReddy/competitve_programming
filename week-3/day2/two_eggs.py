def my_function(arg):
    count=0
    temp=14
    count=0
    while(count<arg):
            z=count
            count=count+temp
            temp=temp-1
            count=count+1
    if(arg==count):
        return count
    count=count+(arg-z)
    return count

for i in range(1,100):
    print(my_function(i))