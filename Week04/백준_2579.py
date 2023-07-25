import sys
sys.stdin  = open('input.txt', 'r')

n = int(input())
step = []

for _ in range(n):
    step.append(int(input()))
step = [0] + step
dp = [[0]*3 for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) # i번 째 계단을 안 밟은 경우 : 전 계단에서 무조건 한 번 or 두 번 연속 밟는 경우 (이 경우 누적합은 두 가지의 경우에서 최댓값)
    dp[i][1] = dp[i-1][0] + step[i] # i번 째 계단을 한 번 밟은 경우 : 전에 계단을 밟지 않아야 함 전에 밟지 않는 경우에서 더 해주기
    dp[i][2] = dp[i-1][1] + step[i] # i번 째 계단을 두 번 연속 밟는 경우 : 전에 계단을 꼭 한 번 밟는 경우! 그 경우에서 현재 계단 더 해주기
print(max(dp[n][1], dp[n][2]))



# n = int(input())
# step = []
# for _ in range(n):
#     step.append(int(input()))
# dp = [0]*n
# if len(step) <= 2:
#     print(sum(step))
# else:
#     dp[0] = step[0]
#     dp[1] = step[0] + step[1]
#     for i in range(2, n):
#         dp[i] = max(dp[i-3] + step[i-1] + step[i], dp[i-2] + step[i])
#     print(dp[-1])





                
                