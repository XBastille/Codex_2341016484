#Name:-Bibhor Puhan
#reg. no:-2341016484
#https://cses.fi/problemset/task/1094
def arara(nums):
    count=0
    for i in range(1, len(nums)):
        if nums[i]<nums[i-1]:
            count+=(nums[i-1]-nums[i])
            nums[i]=nums[i-1]
    return count
n=int(input())
l=list(map(int, input().split()))
q=arara(l)
print(q)
