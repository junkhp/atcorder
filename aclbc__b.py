def main():
    a, b, c, d = map(int, input().split())
    if a < c:
        if c <= b:
            print('Yes')
        else:
            print('No')
    else:
        if a <= d:
            print('Yes')
        else:
            print('No')


if __name__ == "__main__":
    main()
