# import sys
# sys.stdin = open("input.txt", "r")
marks = input()
cnt = 0  # 괄호 개수 추적
result = 0  # 결과 값
i = 0 # 인덱스 돌기 위한 값
while i < len(marks): # 전체를 돌면 반복문 종료
    # 열린 괄호인 경우
    if marks[i] == '(': 
        # 1. 레이저인 경우
        if marks[i + 1] == ')':  
            result += cnt  # 현재까지의 쇠막대기 개수를 결과에 추가
            i += 1  # 레이저는 두 글자이므로 다음 글자로 이동
        # 2. 쇠막대기 시작인 경우
        else:  
            cnt += 1

    # 쇠막대기의 끝인 경우
    else:  
        cnt -= 1
        result += 1  # 끝난 쇠막대기 하나를 결과에 추가

    # 다음 인덱스로 넘어가기 위해서 
    i += 1

print(result)

