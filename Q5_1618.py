#Name:-Bibhor Puhan
#reg. no:-2341016484
#https://cses.fi/problemset/task/1618
def trailing_zeros(num):
    count=0
    while num>=5:
        num//=5
        count+=num
    return count
n=int(input())
c=trailing_zeros(n)
print(c)