# -*- coding: utf-8 -*-

def main():
    sx, sy, gx, gy = map(int, input().split())
    ans = (sy*gx + gy*sx)/(gy + sy)
    print(ans)


if __name__ == '__main__':
    main()
