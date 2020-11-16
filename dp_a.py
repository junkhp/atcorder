# -*- coding: utf-8 -*-
def main():
    n = int(input())
    h = list(map(int, input().split()))

    dp = [0, abs(h[0]-h[1])]
    for i in range(2, n):
        from_2 = dp[i-2] + abs(h[i-2] - h[i])
        from_1 = dp[i-1] + abs(h[i-1] - h[i])
        dp.append(min(from_2, from_1))
    print(dp[-1])


if __name__ == "__main__":
    main()
