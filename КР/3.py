s = input()
l = len(s)
j = 0
for i in range (l//2, l+1):
    a = s[i+1:]
    b = s[i:]
    if(s[l-2*i-1:i] == a[::-1] or s[l-2*i:i] == b[::-1]):
        break
    j+=1
print(j)
