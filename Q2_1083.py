#Name:-Bibhor Puhan
#reg. no:-2341016484
#https://cses.fi/problemset/task/1083
def missingNumber(nums):
    num_set=set(nums)
    return next((num for num in range(1, len(num_set)+1) if num not in num_set), i)
i=int(input())
t=tuple(map(int, input().split()))
m=missingNumber(t)
print(m)