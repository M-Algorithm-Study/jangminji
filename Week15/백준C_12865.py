import sys
sys.stdin  = open('input.txt', 'r')
    
n, k = map(int, input().split())  # n: 물품의 수, k: 가방에 넣을 수 있는 최대 무게
dp = [[0] * (k+1) for _ in range(n+1)]  # 2차원 리스트 dp 초기화 (물품 수 n+1, 가방 무게 k+1)
print(dp)

m = [[0, 0]]  # 물건의 무게와 가치를 저장하는 리스트. 첫 번째 항목은 사용하지 않음.

# 물건의 무게와 가치를 입력받아 m 리스트에 저장
for i in range(n):
    w, v = map(int, input().split())  # w: 각 물건의 무게, v: 물건의 가치
    m.append([w, v])

for i in range(1, n+1):  # 물품을 하나씩 고려하는 반복문
    w = m[i][0]  # 현재 물건의 무게
    v = m[i][1]  # 현재 물건의 가치
    for j in range(1, k+1):  # 가방 무게를 1부터 k까지 하나씩 고려하는 반복문
        if j < w:
            dp[i][j] = dp[i-1][j]  # 현재 물건의 무게가 가방 무게보다 크면 이전 상태를 그대로 가져옴
        else:
            # 현재 물건을 넣을 수 있는 경우, 이전 상태와 현재 물건을 넣었을 때의 가치를 비교하여 더 큰 값을 선택
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])

# dp[n][k]에는 가방에 넣을 수 있는 물건 중 최대 가치가 저장되어 있음
print(dp[n][k])

        



