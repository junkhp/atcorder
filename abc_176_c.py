def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    sum = 0
    now = 0
    for a in a_list:
        if now <= a:
            now = a
        else:
            sum += now-a
    print(sum)
if __name__ == '__main__':
    main()
