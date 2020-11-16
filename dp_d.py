# -*- coding: utf-8 -*-
def main():
    n, w = map(int, input().split())
    weight_list = []
    value_list = []
    wv_list = []
    for i in range(n):
        weight, value = map(int, input().split())
        weight_list.append(weight)
        value_list.append(value)

    dp = [[0] * (w+1) for i in range(n)]
    for i in range(w+1):
        if weight_list[0] <= i:
            dp[0][i] = value_list[0]
    for i in range(1, n):
        for j in range(0, w+1):
            if weight_list[i] <= j:
                # print(dp[i-1][j-weight_list[i]]+value_list[i])
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight_list[i]] + value_list[i])
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[-1][-1])


if __name__ == "__main__":
    main()
