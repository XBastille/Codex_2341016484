#Name:-Bibhor Puhan
#reg. no:-2341016484
#https://cses.fi/problemset/task/1754
def check(a, b):
    if all((a+b)%3==0, a*2>=b, b*2>=a):
        l2.append("YES")
    else:
        l2.append("NO")
l1=[]
l2=[]
n=int(input())
for _ in range(n):
    t=tuple(map(int, input().split()))
    l1.append(t)
for i in l1:
    check(*i)
for i in l2:
    print(i)
