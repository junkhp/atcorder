# -*- coding: utf-8 -*-

def main():
    n = int(input())
    s_list = [input() for i in range(n)]
    check_1 = set()
    check_2 = set()

    for s in s_list:
        if s[0] == '!':
            mozi = s[1:]
            check_2.add(mozi)
            if mozi in check_1:
                print(mozi)
                return
        else:
            check_1.add(s)
            if s in check_2:
                print(s)
                return

    print('satisfiable')

if __name__ == '__main__':
    main()
