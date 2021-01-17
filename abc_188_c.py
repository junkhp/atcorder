# -*- coding: utf-8 -*-
def get_max(player_list):
    max_v = 0
    for i, v in enumerate(player_list):
        if v > max_v:
            max_v = v
            max_index = i
    return max_index, max_v



def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    left_i, left_v = get_max(a_list[: 2 ** (n - 1)])
    right_i, right_v = get_max(a_list[2 ** (n - 1):])
    right_i += 2 ** (n - 1)
    if left_v < right_v:
        print(left_i + 1)
    else:
        print(right_i + 1)


if __name__ == '__main__':
    main()
