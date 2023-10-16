#Name:-Bibhor Puhan
#reg. no:-2341016484
#https://cses.fi/problemset/task/1070
def beautiful_permutation(n):
    if n==1:
        return "1"
    elif n<4:
        return "NO SOLUTION"
    else:
        beautiful_permutation=list(range(2, n+1, 2))
        beautiful_permutation.extend(iter(range(1, n+1, 2)))
        is_beautiful=all(abs(beautiful_permutation[i]-beautiful_permutation[i+1])!=1 for i in range(n-1))
        if is_beautiful:
            return " ".join(map(str, beautiful_permutation))
        else:
            return "NO SOLUTION"
i=int(input())
q=beautiful_permutation(i)
print(q)
