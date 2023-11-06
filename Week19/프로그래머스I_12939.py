def solution(s): 
    result = []
    for i in s.split(" "):
        result.append(int(i))
    max_r = max(result)
    min_r = min(result)
    answer = str(min_r) + " " + str(max_r)

    return answer