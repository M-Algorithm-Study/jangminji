def solution(s):
    words = s.split(" ")
    result = []
    for w in words:
        
        if w != "":
            result.append(w[0].upper() + w[1:].lower())
        else:
            result.append("")

    answer = " ".join(result)
    return answer