import sys
sys.stdin  = open('input.txt', 'r')

# 입력으로 n과 k를 받음
n, k = map(int, input().split())
# 이분탐색으로 차근 차근 나아간다.
# 세로로 자른 경우와 가로로 자른 경우의 차가 작을 경우 조각의 수는 많아지고,
# 클 경우 조각의 수는 적어진다.
# 차근차근 하나씩 자르는게 아니고 처음부터 n번의 경우의 수만 확인

# 왼쪽과 오른쪽 포인터를 초기화
left = 0
right = n // 2

isPossible = False

# 이진 탐색을 사용하여 문제 해결
while left <= right:
    # 현재 가로로 자른 횟수 계산
    rowCut = (left + right) // 2
    # 현재 세로로 자른 횟수 계산
    colCut = n - rowCut
    # 가로와 세로로 자르면 (rowCut + 1) * (colCut + 1) 조각이 생김
    pieces = (rowCut + 1) * (colCut + 1)
    # 조각의 수가 k와 같으면 가능한 경우
    if k == pieces:
        print('YES')
        isPossible = True
        break
    # 조각의 수가 k보다 작으면 더 많이 자름 (오른쪽 범위로 이동)
    if k > pieces:
        left = rowCut + 1
    # 조각의 수가 k보다 크면 덜 자름 (왼쪽 범위로 이동)
    else:
        right = rowCut - 1

# 가능한 경우가 없다면 'NO' 출력
if not isPossible:
    print('NO')



# # 시간 초과ㅠㅠ
# from collections import deque

# n, k = map(int, input().split())
# a = 0
# w, h, cut = 1, 1, 0
# paper = deque([(w, h, cut)])
# result = "NO"

# while cut <= n:
#     # print(paper)
#     nw, nh, cut = paper.popleft()
#     if nw * nh == k and cut == n:
#         result = "YES"
#         break
#     paper.append((nw+1, nh, cut + 1))
#     paper.append((nw, nh+1, cut + 1))

# print(result)

# # 방문리스트를 만들었지만 그래도 시간 초과 ㅜㅜ
# from collections import deque

# n, k = map(int, input().split())
# visited = set()  # 방문한 상태를 저장하기 위한 집합
# result = "NO"

# # 초기 상태를 큐에 추가: (폭, 높이, 가위 사용 횟수)
# queue = deque([(1, 1, 0)])
# cut = 0
# while cut <= n:
#     w, h, cut = queue.popleft()

#     if w * h == k and cut == n:
#         result = "YES"
#         break

#     # 이미 방문한 상태인 경우 스킵
#     if (w, h, cut) in visited:
#         continue

#     # 새로운 상태를 큐에 추가
#     queue.append((w + 1, h, cut + 1))
#     queue.append((w, h + 1, cut + 1))
    
#     # 현재 상태를 방문한 상태로 표시
#     visited.add((w, h, cut))

# print(result)

