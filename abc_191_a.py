# -*- coding: utf-8 -*-
import math
import numpy as np
from numpy import linalg

def main():
    x, y, r = map(float, input().split())
    center = np.array([x, y])
    g_left_up_x, g_left_up_y = x - r, y - r
    g_len = 2 * r
    sin45 = math.sin(math.radians(45))
    cos45 = math.cos(math.radians(45))
    n_left_up_x = x - r * cos45
    n_left_up_y = y - r * sin45
    n_len = 2 * r * cos45

    x0 = g_left_up_x
    x1 = n_left_up_x
    x2 = n_left_up_x + n_len
    x3 = g_left_up_x + g_len
    y0 = g_left_up_y
    y1 = n_left_up_y
    y2 = n_left_up_y + n_len
    y3 = g_left_up_y + g_len
    ans_set = set()

    print(x0)
    print(x1)
    print(x2)
    print(x3)
    # exit()
    ans = (int(x3) - math.ceil(x2)) * \
        (int(y3) - math.ceil(y2))
    print(ans)
    for i_x in range(math.ceil(x0), int(x1) + 1):
        for i_y in range(math.ceil(y0), int(y3) + 1):
            if linalg.norm(np.array([i_x, i_y]) - center) <= r:
                # print(i_x)
                # print(i_y)
                # print('--------')
                ans_set.add((i_x, i_y))

    for i_x in range(math.ceil(x2), int(x3) + 1):
        for i_y in range(math.ceil(y0), int(y3) + 1):
            if linalg.norm(np.array([i_x, i_y]) - center) <= r:
                # print(i_x)
                # print(i_y)
                # print('--------')
                ans_set.add((i_x, i_y))

    for i_x in range(math.ceil(x1), int(x2) + 1):
        for i_y in range(math.ceil(y0), int(y1) + 1):
            if linalg.norm(np.array([i_x, i_y]) - center) <= r:
                # print(i_x)
                # print(i_y)
                # print('--------')
                ans_set.add((i_x, i_y))

    for i_x in range(math.ceil(x1), int(x2) + 1):
        for i_y in range(math.ceil(y2), int(y3) + 1):
            if linalg.norm(np.array([i_x, i_y]) - center) <= r:
                # print(i_x)
                # print(i_y)
                # print('--------')
                
                ans_set.add((i_x, i_y))

    print(ans + len(ans_set))

if __name__ == '__main__':
    main()
