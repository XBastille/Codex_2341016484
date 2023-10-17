#Name:-Bibhor Puhan
#reg. no:-2341016484
#https://cses.fi/problemset/task/1092
def partition(num): 
    total=(num*(num + 1))//2
    if total%2!=0:
        print("NO")
    else:
        print("YES")
        p=total//2
        l1=[]
        l2=[]
        cs=0
        for i in range(num, 0, -1):
            if cs+i<=p:
                l1.append(i)
                cs+=i
            else:
                l2.append(i)
        print(len(l1))
        print(" ".join(map(str, sorted(l1))))
        print(len(l2))
        print(" ".join(map(str, sorted(l2))))
n=int(input())
partition(n)
