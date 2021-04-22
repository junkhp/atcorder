def hantei(a_list, score, k, l):
    kukan_num = 0
    for youkan_len in a_list:
        if youkan_len < score:
            pass
        else:
            kukan_num += 1
        
        if kukan_num == k:
            break
    print('kukan num')
    print(kukan_num)
    if kukan_num < k:
        return False
    else:
        rest_len = l - youkan_len
        # print('yokan len and rest')
        # print(youkan_len)
        # print(rest_len)
        if rest_len >= score:
            return True
        else:
            return False


def main():
    n, l = map(int, input().split())
    k = int(input())
    a_list = list(map(int, input().split()))
    
    for score in range(l, 0, -1):
        if hantei(a_list, score, k, l):
            break
    print(score)

if __name__ == '__main__':
    main()
    
