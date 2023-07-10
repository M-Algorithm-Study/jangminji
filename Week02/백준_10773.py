import sys
N = int(input())
number_list = []
for _ in range(N):
    number = int(sys.stdin.readline())
    if number == 0:
        number_list.pop()
    else:
        number_list.append(number)
print(sum(number_list))