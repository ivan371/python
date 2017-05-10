s = input()
l = len(s)
for i in range(l):
    j = 0
    while(s[i-j:i] == s[i+1:i+j+1] and j <= i and i + j < l):
        j+=1
    print(2*j - 1, end=' ')
