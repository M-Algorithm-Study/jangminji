import sys
sys.stdin  = open('input.txt', 'r')
n = int(input())
electrics = [] 
dp = [1] * n

for _ in range(n):
    a, b = map(int, input().split())
    electrics.append((a, b))

electrics.sort(key=lambda x: (x[0]))

for i in range(n):
    for j in range(i):
        if electrics[j][1] < electrics[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))



    

        
    