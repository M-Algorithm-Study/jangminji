import sys
sys.stdin  = open('input.txt', 'r')
N = int(input())
A = list(map(int, input().split()))  

dp = [1] * (N) 

for i in range(N):  # 1부터 N까지 반복 (수열 A의 각 원소를 순회)
    for j in range(i):  # 현재 원소 A[i] 이전의 원소를 순회
        if A[i] > A[j]:  # 현재 원소 A[i]가 이전 원소 A[j]보다 큰 경우
            dp[i] = max(dp[i], dp[j] + 1)  # dp[i]를 현재까지의 최대 부분 수열 길이와 비교하여 더 큰 값을 선택

print(max(dp))  # dp 리스트에서 가장 큰 값을 출력 (최장 증가 부분 수열의 길이)
