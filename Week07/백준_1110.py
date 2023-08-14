N = input()

if int(N) < 10: 
    N = "0" + N
result = 0
cnt = 0

a = N[1]
b = int(N[0]) + int(N[1])
if b >= 10:
    b = str(b)
    b = b[1]
else:
    b = str(b)

result = a + b
cnt = cnt + 1

while N != result:
    cnt += 1
    a = result[1]
    b = int(result[0]) + int(result[1])
    if b >= 10:
        b = str(b)
        b = b[1]
    else:
        b = str(b)
    result = a + b
    

print(cnt)