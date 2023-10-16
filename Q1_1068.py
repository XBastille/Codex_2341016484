#Name:-Bibhor Puhan
#reg. no:-2341016484
#https://cses.fi/problemset/task/1068
def weird(num):
    while num!=1:
        num=num//2 if num%2==0 else (num*3)+1
        yield num
n=int(input())
print(n)
w=weird(n)
for i in w:
    print(i)
