for _ in range(int(input())):
    l=list(map(int,input().split()))
    n,a,b=l[0],l[1],l[2]
    s=input()
    x=0
    y=0
    for i in s:
        if i=="0":
            x+=1
        else:
            y+=1
    print(x*a+y*b)
            
