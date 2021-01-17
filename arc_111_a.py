# -*- coding: utf-8 -*-

def get_roop(m):
    m_keta_num = len(str(m))
    amari_dict = {}
    for i in range(m_keta_num, m + 1):
        amari = 10 ** i % m
        if amari == 0:
            return -1]
        if amari not in amari_dict.keys():
            amari_dict[amari] = i
        else:
            return amari_dict, amari, 10 ** i // m

def main2():
    n, m = map(int, input().split())
    amari_dict, amari, sho = get_roop(m)
    print(amari)
    print(amari_dict)
    print(sho)
def main():
    n, m = map(int, input().split())
    check_list = [0] * 10
    for i in range(11):
        a = int(10 ** (i + 1) / m)
        num = int(str(a)[-1])
        print(num)
        if num == 0:
            continue
        if num != 0 and check_list[num] == 0:
            check_list[num] = 1
        else:
            length = i
            break
    print(check_list)
    print(a)
    print(length)
    roop_num_str = str(a)[:-1]
    roop_num = int(roop_num_str)

    amari = 10 ** 18 % length
    sho = 10 ** 18 // length
    roop_num_mod = roop_num % m
    first_mod = int(roop_num_str[: amari + 1]) % m
    mod_all = first_mod
    ans = roop_num_str

    x = 0
    for i in range(20):
        x += 10 ** (length*i)
        print(x % m)
        
    print(x)
    # for i in range(n):
    #     ans = ans * 10
    #     print('------------------')
    #     print(ans/m)
    #     print(int(ans/m))
    #     print(int(ans/m) % m)
    # print(int(ans/m) % m)


if __name__ == '__main__':
    main2()
