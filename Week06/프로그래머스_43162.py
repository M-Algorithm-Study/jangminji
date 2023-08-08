def solution(n, computers):
    visited = [[False] * n for _ in range(n)]
    answer = 0
    for i in range(n): # 0 1 2
        if visited[i] == False:
            stack = [i]
            visited[i] = True
            while stack: # 연결된 컴퓨터는 이 while문에서 모두 true로 바뀜
                cur = stack.pop()
                for j in range(n):# 0 1 2
                    if cur == j:
                        continue
                    elif computers[cur][j] == 1 and visited[j] == False:
                        visited[j] = True
                        stack.append(j)
            answer += 1        
    
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))