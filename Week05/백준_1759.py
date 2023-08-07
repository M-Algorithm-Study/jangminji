import sys
sys.stdin  = open('input.txt', 'r')

L, C = map(int, input().split())
alpas = list(input().split())
vowel = ["a", "e", "i", "o", "u"]
visited = [False] * (C+1)
alpas.sort() # ['a', 'c', 'i', 's', 't', 'w']

def backTracking(result):
    # 길이가 같으면 종료 조건
    if len(result) == L:
        # 모음, 자음 개수 카운팅
        a_cnt = 0
        b_cnt = 0
        for r in result:
            if r in vowel:
                a_cnt += 1
            else:
                b_cnt += 1
        if a_cnt >= 1 and b_cnt >= 2:
            print("".join(map(str, result)))
            return
        
    for i in range(len(alpas)): # 0 ~ 5
        if visited[i] == False and (len(result)==0 or alpas[i] > result[-1]):
            visited[i] = True
            result.append(alpas[i])
            backTracking(result)
            visited[i] = False
            result.pop()

backTracking([])