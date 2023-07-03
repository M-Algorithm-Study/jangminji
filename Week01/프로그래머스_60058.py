toggle = lambda x:")" if x=="(" else "("

def split_uv(p):
    cnt = {i:0 for i in "()"}
    for idx, tok in enumerate(p):
        cnt[tok] += 1
        if cnt["("]==cnt[")"]:
            return idx+1
    return -1

def is_correct(p):
    stack = []
    for tok in p:
        if tok=="(":
            stack.append(tok)
        elif stack:
            stack.pop()
        else:
            return False
    return True

def solution(p):
    # 입력이 빈 문자열이거나 올바른 문자열이면 그대로 리턴한다.
    if is_correct(p):
        return p
    # 문자열을 u와 v로 나눈다
    split_idx = split_uv(p)
    u, v = p[:split_idx], p[split_idx:]
    # u가 올바른 문자열이면 v에 대해 1단계부터 다시 수행한 결과를 u에 이어 붙인 후 반환한다.
    if is_correct(u):
        return u+solution(v)
    # 그렇지 않은 경우 "(" 뒤에 v에 대해 1단계부터 다시 수행한 결과를 이어 붙이고, ")"를 다시 붙인다.
    # 이후 u의 양 끝 괄호를 제거하고, 괄호 방향을 뒤집어서 뒤에 이어 붙여 반환한다.
    else:
        return "("+solution(v)+")"+''.join([toggle(i) for i in u[1:-1]])