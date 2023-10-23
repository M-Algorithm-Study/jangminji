import sys
sys.stdin  = open('input.txt', 'r')

N = int(input())
numbers = list(map(int, input().split()))
plus, minus, murti, div = map(int, input().split())
max_result = - int(1e9)
min_result = int(1e9)

def dfs(depth, total, plus, minus, murti, div):
    global max_result, min_result

    if depth == N:
        # print("인덱스가 N이 됨")
        max_result = max(max_result, total)
        min_result = min(min_result, total)
        return
    
    if plus:
        # print(numbers[depth], "+")
        dfs(depth + 1, total + numbers[depth], plus - 1, minus, murti, div)

    if minus:
        # print(numbers[depth], "-")
        dfs(depth + 1, total - numbers[depth], plus, minus - 1, murti, div)

    if murti:
        # print(numbers[depth], "*")
        dfs(depth + 1, total * numbers[depth], plus, minus, murti - 1, div)

    if div:
        # print(numbers[depth], "/")
        dfs(depth + 1, int(total / numbers[depth]), plus, minus, murti, div - 1)


dfs(1, numbers[0], plus, minus, murti, div)
print(max_result)
print(min_result)


# a = 3
# b = -17
# print(b//a)

