delta_dict = {
    "R" : [0, 1], "L" : [0, -1],
    "B" : [1, 0], "T" : [-1, 0],
    "RT" : [-1, 1], "LT" : [-1, -1],
    "RB" : [1, 1], "LB" : [1, -1]
}
k, r, N = input().split()

king = [8 - int(k[1]), ord(k[0]) - 65]
rock = [8 - int(r[1]), ord(r[0]) - 65]
move_list = []

for _ in range(int(N)):
    n_king = [0,0]
    move = input()
    move = delta_dict[move]
    n_king[0] = king[0] + move[0]
    n_king[1] = king[1] + move[1]

    # +한 킹이 범위 안에 있는 경우
    if 0 <= n_king[0] <= 7 and  0 <= n_king[1] <= 7:

        # +한 킹과 돌의 위치가 같으면
        if n_king == rock:
            # 그 돌이 범위 안에 있으면
            if 0 <= rock[0] + move[0] <= 7 and 0 <= rock[1] + move[1] <= 7:
                rock[0] = rock[0] + move[0]
                rock[1] = rock[1] + move[1]
                king = n_king
            # 돌이 범위 안에 없으면
            else:
                continue
        # 돌의 위치와 킹의 위치가 같지 않으면
        else:
            king = n_king
    # + 킹이 범위 안에 없는 경우
    else:
        continue
print(chr(king[1]+65), 8 - king[0], sep="")
print(chr(rock[1]+65), 8 - rock[0], sep="")