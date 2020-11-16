def main():
    n, m, k = map(int, input().split())
    shigemi = [0] * n
    place_dic = {}
    for i in range(m):
        place = int(input())
        shigemi[place - 1] = 1
        place_dic[i+1] = place-1
    for i in range(k):
        for usagi in range(1, m + 1):
            np = place_dic[usagi]
            shigemi[np] = 0
            for j in list(range(np + 1, n)) + list(range(np + 1)):
                if shigemi[j] == 0:
                    shigemi[j] = 1
                    place_dic[usagi] = j
                    break

    for i in range(1, m + 1):
        print(place_dic[i] + 1)


if __name__ == "__main__":
    main()
