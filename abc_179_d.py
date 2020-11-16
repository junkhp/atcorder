def main():
    n, k = map(int, input().split())
    move_set = set([])

    for i in range(k):
        a, b = map(int, input().split())
        for j in range(a, b + 1):
            move_set.add(j)
    sorted_set = sorted(move_set)
    # print(sorted_set)
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n+1):
        for num in sorted_set:
            if num + 1 > i:
                break
            else:
                dp[i] += dp[i - num]
    print(dp[-1] % 998244353)


if __name__ == "__main__":
    main()
