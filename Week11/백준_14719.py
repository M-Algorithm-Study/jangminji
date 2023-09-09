import sys
sys.stdin  = open('input.txt', 'r')
from collections import deque
H, W = map(int, input().split())
block_list = deque(map(int, input().split()))

# 빈 그래프 만들기
word = []
for _ in range(H):
    word.append([0] * W)

# 블록 채우기
b = -1
for _ in range(W):
    b_h = block_list.popleft()
    a = H-1
    b += 1
    for _ in range(b_h):
        word[a][b] = 1
        a -= 1
rain = 0

# 전체 그래프 돌기
for i in range(H):
    for j in range(W):
        if word[i][j] == 1:
            cnt = 0
            while True:
                j += 1
                if j == W:
                    break
                elif word[i][j] == 1:
                    rain += cnt
                    break
                elif word[i][j] == 0:
                    cnt += 1
                    word[i][j] = 3
                
print(rain)

        
