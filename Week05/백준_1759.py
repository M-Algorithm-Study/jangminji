import sys
sys.stdin  = open('input.txt', 'r')
L, C = map(int, input().split())
alpas = list(input().split())
vowel = ["a", "e", "i", "o", "u"]
visited = [False] * (C+1)
alpas.sort()
# print(alpas)
def backTracking(result):
    if len(result) == L:
        v_cnt = 0
        a_cnt = 0
        for a in result:
            if a in vowel:
                v_cnt += 1
            else:
                a_cnt += 1
        if v_cnt >= 1 and a_cnt >= 2:
            print("".join(map(str, result)))
            
            return
    for i in range(len(alpas)):
        if (len(result)==0 or alpas[i] > result[-1]):
            # visited[i] = True
            result.append(alpas[i])
            backTracking(result)
            # visited[i] = False
            result.pop()
backTracking([])