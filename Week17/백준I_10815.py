import sys
sys.stdin  = open('input.txt', 'r')

N = int(input())
card = sorted(list(map(int, input().split())))

M = int(input())
checks = list(map(int, input().split()))

for check in checks:
    left, right = 0, N - 1
    flag = False
    while left <= right:
        mid = (left + right) // 2
        if card[mid] > check:
            right = mid - 1

        elif card[mid] < check:
            left = mid + 1
        
        else:
            flag = True
            break
    if flag:
        print(1, end=" ")
    else:
        print(0, end=" ")





# import sys

# N = int(sys.stdin.readline())
# cards = sorted(list(map(int, sys.stdin.readline().split())))
# M = int(sys.stdin.readline())
# checks = list(map(int, sys.stdin.readline().split()))

# for check in checks:
#     low, high = 0, N-1  # cards의 이진 탐색 index
#     exist = False
#     while low <= high:
#         mid = (low + high) // 2
#         if cards[mid] > check:  # 중간 값보다 작다면
#             high = mid - 1  # 중간보다 왼쪽 한 칸 옆까지 탐색
#         elif cards[mid] < check:  # 중간 값보다 크다면
#             low = mid + 1  # 중간보다 오른쪽 한 칸 옆부터 탐색
#         else:
#             exist = True
#             break
#     print(1 if exist else 0, end=' ')

