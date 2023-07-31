import sys
sys.stdin  = open('input.txt', 'r')
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

def backTracking(result):
    if len(result) == M:
        print(*result)
        return
    for i in range(len(num_list)):
        if (len(result)==0 or num_list[i] >= result[-1]): 

            result.append(num_list[i])
            backTracking(result)
            result.pop()
backTracking([])