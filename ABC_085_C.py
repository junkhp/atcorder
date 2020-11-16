# -*- coding: utf-8 -*-
def main():
    N, Y = map(int, input().split())
    now = 0
    check = 0
    for i in range(0, N + 1):
        for j in range(0, N+1-i):
            k = N - i - j
            sum = 10000*i + 5000*j + 1000*k

            if sum == Y:
                print(str(i) + ' ' + str(j) + ' ' + str(k))
                return
            elif sum > Y:
                break
    print('-1 -1 -1')
    return


if __name__ == '__main__':
    main()
