def main():
    a,b,c,d = map(int, input().split())
    max = -1000000000000000000000
    for x in [a, b]:
        for y in [c, d]:
            if x*y > max:
                max = x*y
    print(max)



if __name__ == '__main__':
    main()
