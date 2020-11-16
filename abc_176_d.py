import numpy as np
from collections import deque

def check_func(h, w, check, meiro):
    if (h >= 0 and w >= 0) and (h < len(meiro) and w < len(meiro[0])) and meiro[h][w] == '.' and not (h, w) in check:
        return True
    else:
        return False
def main():
    h, w = map(int, input().split())
    sh, sw = map(int, input().split())
    gh, gw = map(int, input().split())
    s_meiro = []
    for i in range(h):
        s_meiro.append(list(input()))
    check_list = np.full((h, w), -1)
    start = [sh-1, sw-1]
    goal = [gh-1, gw-1]
    now_cost = 0
    checked_point = set()
    cost_1_set = set()
    point_que = deque([start])
    cost_dict = {tuple(start): now_cost}

    move_walk = [[-1, 0], [1, 0], [0, -1,], [0, 1]]
    move_warp = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            if not [i, j] in move_walk and [i, j] != [0,0]:
                move_warp.append([i, j])

    ans = -1
    while(1):
        # print('----------------')
        # print(point_que)
        # print(cost_dict)
        check_point = point_que.popleft()
        # 歩く
        for masu in move_walk:
            ph, pw = check_point[0] - masu[0], check_point[1] - masu[1]
            cost = cost_dict[tuple(check_point)]
            if (ph, pw) in cost_1_set:
                cost_1_set.discard((ph, pw))
                try:
                    point_que.remove([ph, pw])
                except:
                    pass
                point_que.appendleft([ph, pw])
                cost_dict[(ph, pw)] = cost
            if check_func(ph, pw, checked_point, s_meiro):
                checked_point.add((ph, pw))
                point_que.appendleft([ph, pw])
                cost_dict[(ph, pw)] = cost
        # 魔法で移動
        for masu in move_warp:
            ph, pw = check_point[0] - masu[0], check_point[1] - masu[1]
            cost = cost_dict[tuple(check_point)]
            if check_func(ph, pw, checked_point, s_meiro):
                cost += 1
                checked_point.add((ph, pw))
                point_que.append([ph, pw])
                cost_dict[(ph, pw)] = cost
                cost_1_set.add((ph, pw))



        if len(point_que) == 0:
            break
    try:
        print(cost_dict[tuple(goal)])
    except:
        print(-1)



if __name__ == '__main__':
    main()
