def main():
    n, k = map(int, input().split())
    move_set = set([])

    for i in range(k):
        a, b = map(int, input().split())
        move_set.add(a)
        move_set.add(b)
    sorted_set = sorted(move_set)
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(1, n+1):
        for num in sorted_set:
            if i + num <= n:
                dp[i + num] += dp[i]
            else:
                break
    # print(dp[-1] % 998244353)
    print(dp)


if __name__ == "__main__":
    main()
