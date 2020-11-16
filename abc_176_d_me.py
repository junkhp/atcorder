import numpy as np

def show_merio(meiro):
    for i in meiro:
        print(i)

def check(area1, area2):
    area2_set = set(map(tuple, area2))
    new_area1 = []
    for p in area1:
        for i in range(p[0]-2, p[0] + 3):
            for j in range(p[1]-2, p[1] + 3):
                new_area1.append((i, j))
        if len(set(new_area1) & area2_set) != 0:
            return True
    return False


def main():
    h, w = map(int, input().split())
    ch, cw = map(int, input().split())
    dh, dw = map(int, input().split())
    s_meiro = []
    for i in range(h):
        s_meiro.append(list(input()))
    print(s_meiro)

    area = [[0 for j in range(w)] for i in range(h)]
    area_dict = {}
    area_id = 1
    for i in range(h):
        for j in range(w):
            show_merio(area)
            if s_meiro[i][j] == '.':
                if i != 0:
                    up_id = area[i-1][j]
                else:
                    up_id = 0
                if j != 0:
                    left_id = area[i][j-1]
                else:
                    left_id = 0
                # if i == 0 and j== 0:
                #     area[i][j] = area_id
                #     area_id += 1
                print(str(i+1) + ':' +str(j+1))
                print(up_id, end=' ')
                print(left_id)
                print('------------')
                if up_id == 0 and left_id == 0:
                    area[i][j] = area_id
                    if not area_id in area_dict.keys():
                        area_dict[area_id] = [[i+1, j+1]]
                    else:
                        area_dict[area_id].append([i+1, j+1])
                    area_id += 1
                else:
                    if up_id == left_id:
                        area[i][j] = up_id
                        if not up_id in area_dict.keys():
                            area_dict[up_id] = [[i+1, j+1]]
                        else:
                            area_dict[up_id].append([i+1, j+1])
                    elif up_id*left_id == 0:
                        area[i][j] = max(up_id, left_id)
                        if not area[i][j] in area_dict.keys():
                            area_dict[area[i][j]] = [[i+1, j+1]]
                        else:
                            area_dict[area[i][j]].append([i+1, j+1])
                    else:
                        area[i][j] = min(up_id, left_id)
                        area_dict[area[i][j]] += area_dict[max(up_id, left_id)]
                        area_dict.pop(max(up_id, left_id))
    area_list = [[0 for j in range(w)] for i in range(h)]
    keys = list(area_dict.keys())
    for i in range(len(keys)-1):
        for j in range(i+1, len(keys)):
            if check(area_dict[keys[i]], area_dict[keys[j]]):
                print('yes')



    print(area_dict)



if __name__ == '__main__':
    main()
