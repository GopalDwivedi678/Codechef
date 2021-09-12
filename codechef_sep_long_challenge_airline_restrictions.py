for i in range(int(input())):
    l=list(map(int,input().split()))
    if (l[0]+l[1]<=l[3] and l[2]<=l[4]):
        print("YES")
    elif (l[1]+l[2]<=l[3] and l[0]<=l[4]):
        print("YES")
    elif (l[0]+l[2]<=l[3] and l[1]<=l[4]):
        print("YES")
    else:
        print("NO")
