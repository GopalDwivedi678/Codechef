for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x,y=0,0
    for i in a:
        if i%2==0:
            x+=1
        else:
            y+=1
    o,e=n//2,n//2
    if n%2==1:
        o+=1
    print(min(o,x)+min(e,y))
            
