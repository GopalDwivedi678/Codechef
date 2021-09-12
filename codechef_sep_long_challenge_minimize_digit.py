for _ in range(int(input())):
    z=list(map(int,input().split()))
    n,l,r=z[0],z[1],z[2]
    if (n>=l and n<=r):
        print(n)
        continue
    if (n<l):
        print(l)
    s1=0
    s2=1000000
    m=0
    while(l<r and (n/r)<r):
        temp1=n/r
        temp2=n%r
        if (s2>temp1+temp2):
            s2=temp1+temp2
            m=r
        r=n/(temp1+1)
    while(l<=r):
        e=n
        s1=0
        while(True):
            if (e<l):
                s1+=e
                if s1<s2:
                    m=l
                    s2=s1
                break
            s1+=e%l
            e/=l
            if s1>=s2:
                break
        l+=1
    print(m)
        
