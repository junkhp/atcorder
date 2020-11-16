# -*- coding: utf-8 -*-
from collections import deque


def main():
    h, w = map(int, input().split())
    a = '.'
    b = '#'
    s_list = [[b] * (w + 2)]
    for i in range(h):
        s_list.append([b] + list(input()) + [b])
    s_list.append([b] * (w + 2))

    tansaku_list = [[0]*(w+2)]
    for i in range(h):
        tansaku_list.append([0] + [[0, (-1, -1)] for i in range(w + 2)] + [0])
    tansaku_list.append([0]*(w+2))

    for x in tansaku_list:
        print(x)

    tate_num = 0
    yoko_num = 0
    tate_tansaku_dic = {}
    yoko_tansaku_dic = {}
    one_masu_list = []
    mod = 1000000007
    for i in range(1, h+1):
        for j in range(1, w + 1):
            if s_list[i][j] == a:
                tansaku_list[i][j][0] = -1
                continue
            if s_list[i][j + 1] == b and s_list[i + 1][j] == b:
                tansaku_list[i][j][0] = 3
                one_masu_list.append((i, j))
                continue

            # 完全未探索
            if tansaku_list[i][j][0] == 0:
                # 横に探索
                x = i
                y = j
                area = [y]
                y += 1
                while (1):
                    if s_list[x][y] == b:
                        break
                    area.append(y)
                    tansaku_list[x][y][0] = 1
                    tansaku_list[x][y][1][1] = yoko_num
                    y += 1
                yoko_tansaku_dic[yoko_num] = [x, area]
                yoko_num += 1

                縦に探索

                x = i
                y = j
                area = [y]
                y += 1
                while (1):
                    if s_list[x][y] == b:
                        break
                    area.append(y)
                    tansaku_list[x][y][0] = 1
                    tansaku_list[x][y][1][1] = yoko_num
                    y += 1
                yoko_tansaku_dic[yoko_num] = [x, area]
                yoko_num += 1

                pass
            else:
                pass


if __name__ == "__main__":
    main()
