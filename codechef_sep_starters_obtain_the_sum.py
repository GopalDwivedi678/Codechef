try:
    for _ in range(int(input())):
        n,s=map(int,input().split())
        x=(n*(n+1))//2-s
        if x>=1 and x<=n:
            print(x)
        else:
            print(-1)
except:
    pass
