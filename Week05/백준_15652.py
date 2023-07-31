N, M = map(int, input().split()) # 3 3

def backTracking(result): 
    # M과 리스트의 개수가 같으면 출력 후 함수 종료
    if len(result) == M: 
        print(*result)
        return
   
    for i in range(1, N+1): # 1 2 3
        if len(result)==0 or i >= result[-1]: # 리스트 마지막 값이 반복문 i값보다 같거나 크면 i append
            result.append(i) 
            # 재귀로 백트래킹 실행
            backTracking(result) 
            result.pop() 

backTracking([])