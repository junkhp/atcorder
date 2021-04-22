# -*- coding: utf-8 -*-
def main():
    n = int(input())
    ab_list = [list(map(int, input().split())) for i in range(n)]

    a_dict = {}
    b_dict = {}
    for i, ab in enumerate(ab_list):
        a = ab[0]
        b = ab[1]
        if a in a_dict.keys():
            a_dict[a].append(i)
        else:
            a_dict[a] = [i]
        
        if b in b_dict.keys():
            b_dict[b].append(b)
        else:
            b_dict[b] = [i]

    a_keys = sorted(a_dict.keys())
    b_keys = sorted(b_dict.keys())


    if len(a_keys) == 1 or len(b_keys) == 1:
        print(max(a_keys[0], b_keys[0]))
        return

    top_a_key = a_keys[0]
    top_b_key = b_keys[0]
    second_a_key = a_keys[1]
    second_b_key = b_keys[1]

    if len(a_dict[top_a_key]) == 1 and len(b_dict[top_b_key]) == 1 and a_dict[top_a_key] == b_dict[top_b_key]:
        print(min(top_a_key + top_b_key, max(top_a_key, second_b_key), max(second_a_key, top_b_key)))
    else:
        print(max(top_a_key, top_b_key))


if __name__ == '__main__':
    main()
