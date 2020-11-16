def main():
    n, m = map(int, input().split())
    road_list = [list(map(int, input().split())) for i in range(m)]
    print(road_list)


if __name__ == "__main__":
    main()
