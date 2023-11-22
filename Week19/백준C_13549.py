# from collections import deque

# N, K = map(int, input().split())
# visited = [-1] * 100001
# q = deque([N])
# visited[N] = 0
# cnt = 0
# while q:
#     cur = q.popleft()
#     cnt += 1
#     # print("cnt", cnt, "cur", cur)
#     if cur == K:
#         print(visited[cur])
#         break
#     for i in (cur * 2, cur + 1, cur - 1):
#         if 0 <= i <= 100000 and (visited[i] == -1 or visited[i] > visited[cur]):
#             if i == (cur * 2):
#                 visited[i] = visited[cur]
#                 q.appendleft(i)
                
#             else:
#                 visited[i] = visited[cur] + 1
#                 q.append(i)
# 왜 틀렸다고 나와요.....ㅜㅠ 해결!


import sys
input = sys.stdin.readline

from collections import deque

n, m=map(int, input().split())
g = [0]*100001
q = deque([n])
# 처음 시작 1로 초기화 / 실제론 0이지만 구별하기 위해 설정
g[n] = 1

while q:
    x = q.popleft()

    # 동생을 찾으면 출력
    if x == m:
        print(g[m] - 1)
        break

    # 3가지 상황을 모두 반복
    for nx in (2*x, x-1, x+1):
        # 구간 내이고, 방문하지 않았으면
        if 0 <= nx <= 100000 and not g[nx]:
            # *2인 경우
            if nx == 2*x:
                # 0초 증가
                g[nx] = g[x]
                q.append(nx)
            # -1, +1인 경우
            else:
                # 1초 증가
                g[nx] = g[x] + 1
                q.append(nx)