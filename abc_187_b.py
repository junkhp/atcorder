# -*- coding: utf-8 -*-
def main():
    n = int(input())
    xy_list = [list(map(int, input().split())) for i in range(n)]
    cnt = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            katamuki = (xy_list[i][1] - xy_list[j][1]) / (xy_list[i][0] - xy_list[j][0])
            if -1 <= katamuki and katamuki <= 1:
                cnt += 1
    print(cnt)
if __name__ == '__main__':
    main()
