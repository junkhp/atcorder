# -*- coding: utf-8 -*-


def main():
    a, b = map(int, input().split())
    b_list = list(map(int, list(str(b))))
    a_list = list(map(int, list(str(a))))

    if sum(a_list) < sum(b_list):
        print(sum(b_list))
    else:
        print(sum(a_list))

if __name__ == '__main__':
    main()
