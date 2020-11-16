def main():
    h, w, m = map(int, input().split())
    h_bomb_dict = {}
    w_bomb_dict = {}
    bombs = []
    for i in range(m):
        zh, zw = map(int, input().split())
        bombs.append((zh, zw))
        if zh in h_bomb_dict.keys():
            h_bomb_dict[zh] += 1
        else:
            h_bomb_dict[zh] = 1

        if zw in w_bomb_dict.keys():
            w_bomb_dict[zw] += 1
        else:
            w_bomb_dict[zw] = 1
    bombs = set(bombs)

    hbombs = max(h_bomb_dict.values())
    wbombs = max(w_bomb_dict.values())
    h_maxs = []
    w_maxs = []
    for key, v in h_bomb_dict.items():
        if v == hbombs:
            h_maxs.append(key)

    for key, v in w_bomb_dict.items():
        if v == wbombs:
            w_maxs.append(key)

    for h in h_maxs:
        for w in w_maxs:
            if not (h, w) in bombs:
                print(hbombs + wbombs)
                return
    print(hbombs + wbombs-1)
if __name__ == '__main__':
    main()
