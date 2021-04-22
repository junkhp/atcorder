# -*- coding: utf-8 -*-
def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))

    sub_set = set(a_list[:m])
    print(sub_set)
    for i in range(n):
        if i not in sub_set:
            min_num = i
            break
    print(min_num)

if __name__ == '__main__':
    main()
