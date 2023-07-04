def parse(str):
    # '올바른 괄호 문자열'인지 확인하는 변수
    correct = True
    # 열린 괄호 카운팅
    left = 0
    # 닫힌 괄호 카운팅
    right = 0
    mystack = []

    for i in range(len(str)):
        if str[i] == '(':
            left += 1
            mystack.append('(')
        else:
            right += 1
            # 쌍이 맞지 않는 경우
            if len(mystack) == 0:
                correct = False
            # 쌍이 맞는 경우
            else:
                mystack.pop()
        # 처음으로 '균형잡힌 괄호 문자열'인 경우에 함수 반환
        # u가 '올바른 괄호 문자열'인 경우에 correct는 True 한번이라도 맞지 않았으면 False
        if left == right:
            return i + 1, correct
        
    # 문제에선 항상 '균형잡인 괄호 문자열'만 주어지기 때문에 위에 for문에서 함수는 종료 되지만! 혹시나 하는 마음에...
    return 0, False

# p는 항상 '균형잡인 괄호 문자열'
def solution(p):
    # 빈 문자열 일 때 그대로 반환
    if len(p) == 0:
        return p
    
    # 빈 문자열이 아닌 경우 u, v로 분리
    else:
        pos, correct = parse(p)
        u = p[:pos]
        v = p[pos:]

        # u가 '올바를 괄호 문자열'이면
        if correct:
            # 재귀로 함수 호출 후 u뒤에 붙여서 반환
            return u + solution(v)

        # u가 '올바른 괄호 문자열'이 아니면 
        # ( + 재귀한 v + ) + u의 첫번 째 마지막 제거 후 괄호 방향 뒤집기 
        else:
            # ( + 재귀한 v + )
            answer = '(' + solution(v) + ')'

            # u의 첫 번째 마지막 제거 후 괄호 방향 뒤집기
            for i in range(1, len(u)-1):
                if u[i] == '(':
                    answer += ')'
                else:
                    answer += '('
            return answer

# 이전 풀이
# toggle = lambda x:")" if x=="(" else "("

# def split_uv(p):
#     cnt = {i:0 for i in "()"}
#     for idx, tok in enumerate(p):
#         cnt[tok] += 1
#         if cnt["("]==cnt[")"]:
#             return idx+1
#     return -1

# def is_correct(p):
#     stack = []
#     for tok in p:
#         if tok=="(":
#             stack.append(tok)
#         elif stack:
#             stack.pop()
#         else:
#             return False
#     return True

# def solution(p):
#     # 입력이 빈 문자열이거나 올바른 문자열이면 그대로 리턴한다.
#     if is_correct(p):
#         return p
#     # 문자열을 u와 v로 나눈다
#     split_idx = split_uv(p)
#     u, v = p[:split_idx], p[split_idx:]
#     # u가 올바른 문자열이면 v에 대해 1단계부터 다시 수행한 결과를 u에 이어 붙인 후 반환한다.
#     if is_correct(u):
#         return u+solution(v)
#     # 그렇지 않은 경우 "(" 뒤에 v에 대해 1단계부터 다시 수행한 결과를 이어 붙이고, ")"를 다시 붙인다.
#     # 이후 u의 양 끝 괄호를 제거하고, 괄호 방향을 뒤집어서 뒤에 이어 붙여 반환한다.
#     else:
#         return "("+solution(v)+")"+''.join([toggle(i) for i in u[1:-1]])