def base(s):
    d={}
    for i in range(len(s)):
        d[i]=s[i]
    return d
count=0
short_url={}
first_url={}
base62=base("abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def generate_short_url(url):
    if (url in first_url):
        print("Duplicate url is"+first_url[url])
        return
    global count
    st=""
    su=count
    count+=1
    if (su==0):
        st="0000000"
        if (st not in short_url):
            short_url[st]=url
            first_url[url]=st
            print("shortened url for"+url+" is "+st)
            return
    while(su!=0):
        st=base62[su%62]+st
        su=su//62
    l=len(st)
    if (l<7):
        for i in range(7-l):
            st="0"+st
    if (st not in short_url):
        short_url[st]=url
        first_url[url]=st
    print("short url for the "+url+" is https://ca.ke/"+st)

while (True):
    print("Enter \n\t1) generate Shorturl\n\t2)redirect Shorturl")
    userInput=int(input())
    if (userInput==1):
        url=input("url:")
        generate_short_url(url)
    elif (userInput==2):
        shortURL=input("Enter a short url: ")
        if short_url.get(shortURL,None) is not None:
            print("Go to url:"+short_url[shortURL])
        else:
            print("not present")
    else:
        print("invalid")