# -*- coding: utf-8 -*-
def main():
    h, w = map(int, input().split())
    s_list = [list(input()) for i in range(h)]

    a = '.'
    b = '#'
    ans = 0

    for i in range(h):
        for j in range(w):
            if i == h - 1 and j == w - 1:
                continue
            elif i == h - 1:
                if s_list[i][j] == a and s_list[i][j + 1] == a:
                    ans += 1
            elif j == w - 1:
                if s_list[i][j] == a and s_list[i+1][j] == a:
                    ans += 1
            else:
                if s_list[i][j] == a and s_list[i][j + 1] == a:
                    ans += 1
                if s_list[i][j] == a and s_list[i + 1][j] == a:
                    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
