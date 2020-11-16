# -*- coding: utf-8 -*-
def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))

    dp = [0, abs(h[0] - h[1])]
    for i in range(2, n):
        min_cost = float('inf')
        for j in range(max(i - k, 0), i):
            cost = dp[j] + abs(h[j] - h[i])
            if min_cost > cost:
                min_cost = cost
        dp.append(min_cost)

    print(dp[-1])


if __name__ == "__main__":
    main()
