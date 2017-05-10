s = input()
l = len(s)
for i in range(l):
    j = 0
    a = s[i+1:i+j+1]
    while(s[i-j:i] == a[::-1] and j <= i and i + j < l):
        j+=1
        a = s[i+1:i+j+1]
    print(2*j - 1, end=' ')
