#Name:-Bibhor Puhan
#reg. no:-2341016484

def repetitions(chara):
    count=1  
    max_count=1
    for i in range(len(chara)):
        try:
            if chara[i+1]==chara[i] :
                count+=1
            else:
                count=1
                prev_char=chara[i]
        except IndexError:
            pass
        max_count=max(max_count, count)
    return max_count
s=input()
r=repetitions(s)
print(r)


        
