from itertools import permutations
def perm(word):
    q=tuple(permutations(word))
    n={"".join(q[i]) for i in range(len(q))}
    t=sorted(n)
    print(len(t))
    for i in t:
        print(i)
s=input()
perm(s)