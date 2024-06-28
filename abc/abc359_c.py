s = list(map(int, input().split()))
t = list(map(int, input().split()))

if (s[0]+s[1])%2 == 1:
    s[0] -= 1
if (t[0]+t[1])%2 == 1:
    t[0] -= 1
    
x = abs(t[0]-s[0])
y = abs(t[1]-s[1])
result = 0
if x < y:
    result = y
else:
    result = (x+y) // 2
print(result)
