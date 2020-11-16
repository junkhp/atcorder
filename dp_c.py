# -*- coding: utf-8 -*-
def main():
    n = int(input())
    abc_list = []
    for i in range(n):
        abc_list.append(list(map(int, input().split())))
    dp = [[0] * 3 for i in range(n)]
    dp[0][0] = abc_list[0][0]
    dp[0][1] = abc_list[0][1]
    dp[0][2] = abc_list[0][2]
    # print(dp)
    for i in range(1, n):
        dp[i][0] = abc_list[i][0] + max(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = abc_list[i][1] + max(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = abc_list[i][2] + max(dp[i - 1][0], dp[i - 1][1])
        # print(dp)
    print(max(dp[-1]))


if __name__ == "__main__":
    main()
