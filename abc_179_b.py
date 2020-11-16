def main():
    n = int(input())
    count = 0
    for i in range(n):
        x, y = map(int, input().split())
        if x == y:
            count += 1
        else:
            count = 0

        if count == 3:
            print('Yes')
            return
    print('No')


if __name__ == "__main__":
    main()
