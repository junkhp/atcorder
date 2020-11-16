# -*- coding: utf-8 -*-
def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    dp = [[0] * len_t for i in range(len_s)]

    for j in range(len_t):
        if s[0] == t[j]:
            for k in range(j, len_t):
                dp[0][k] = 1
            break

    for i in range(len_s):
        if s[i] == t[0]:
            for k in range(i, len_s):
                dp[k][0] = 1
            break

    for i in range(1, len_s):
        for j in range(1, len_t):
            if s[i] == t[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    length = dp[-1][-1]
    i = len_s - 1
    j = len_t - 1
    ans = ''
    while (length > 0):
        if s[i] == t[j]:
            ans = s[i] + ans
            i -= 1
            j -= 1
            length -= 1
        elif (j > 0 and dp[i][j - 1] == dp[i][j]) or i == 0:
            j -= 1
        else:
            i -= 1

    # for d in dp:
    #     print(d)

    print(ans)


if __name__ == "__main__":
    main()
