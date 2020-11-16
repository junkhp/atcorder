def check(atcg_dict):
    if atcg_dict['A'] == atcg_dict['T'] and atcg_dict['C'] == atcg_dict['G']:
        return True
    else:
        return False


def main():
    n, s = input().split()
    n = int(n)
    ans = 0
    atcg_bool_dict = {}
    atcg_dict = {}
    i = 2
    mozi2_list = []
    for j in range(0, n - i + 1):
        count_dict = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        moziretu = s[j: j + i]
        mozi2_list.append(moziretu)
        for mozi in moziretu:
            count_dict[mozi] += 1
        atcg_dict[moziretu] = count_dict

        if check(count_dict):
            ans += 1
        atcg_bool_dict[moziretu] = check(count_dict)
    # print(mozi2_list)

    # print(atcg_dict)

    moziall_list = [mozi2_list]
    for i in range(n // 2):
        i_new = (i + 1) * 2
        mozin_list = []
        # print('---------------------')
        # print(i)
        # print(i_new)
        for j in range(len(moziall_list[i])):
            # print('--------')
            # print(i_new + j)
            if i_new + j >= len(mozi2_list):
                break
            moziretu_b = mozi2_list[i_new + j]
            moziretu_b_num = atcg_dict[moziretu_b]
            moziretu_a = moziall_list[i][j]
            moziretu_a_num = atcg_dict[moziretu_a]
            count_dict = {}
            for k in ['A', 'T', 'C', 'G']:
                count_dict[k] = moziretu_a_num[k] + moziretu_b_num[k]
            atcg_dict[moziretu_a + moziretu_b] = count_dict
            if check(count_dict):
                ans += 1
            mozin_list.append(moziretu_a + moziretu_b)
        moziall_list.append(mozin_list)
    # for i in moziall_list:
    #     print(i)

    print(ans)


if __name__ == "__main__":
    main()
