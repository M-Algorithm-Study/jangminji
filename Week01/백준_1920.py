import sys
sys.stdin = open("input.txt", "r")
N = int(input())
A_list = set(map(int, input().split()))
# print(A_list)
M = int(input())
numbers = map(int, input().split())

for i in numbers:
    if i in A_list:
        print(1)
    else:
        print(0)

# import sys
# input = sys.stdin.readline
# N = int(input())
# num_list = list(map(int, input().split()))
# M = int(input())
# target_list = list(map(int, input().split()))

# num_list.sort()
# for target in target_list:
#     start = 0
#     end = len(num_list)-1
#     cnt = 0
#     while start <= end:
#         mid = (start+end)//2
#         if num_list[mid] == target:
#             cnt += 1
#             break
#         elif num_list[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     print(cnt)