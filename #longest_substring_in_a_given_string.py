#longest substring in a given string

def longSubstring(s):
    charSet = []
    l=0
    li = []
    ss = ''
    for r in range(len(s)):
     
        if s[r] not in ss:
            ss+= s[r]
        else:
            li.append(ss)            
            ss = ''

        
        
    return li        


ret = longSubstring('abcdbabcbb')
print(ret)
#print(max(ret,key=len))


