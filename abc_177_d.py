# -*- coding: utf-8 -*-
# def get_group_num(sum, nums):
#     if len(nums) == 1:
#         return sum + nums[0]
#     pass

def main():
    n, m = map(int, input().split())
    friends_list = []
    num_check = {}
    numnum = {}
    set_num = 1
    for i in range(m):
        check=True
        a,b = map(int, input().split())
        if a in num_check.keys() and a in num_check.keys():
            pass
        elif a in num_check.keys():
            num_check[b] = num_check[a]
            numnum[num_check[a]] += 1
        elif a in num_check.keys():
            num_check[a] = num_check[b]
            numnum[num_check[b]] += 1
        else:
            num_check[a] = set_num
            num_check[b] = set_num
            numnum[set_num] = 2
            set_num += 1



        #
        #
        #
        #
        # for i, friends_set in enumerate(friends_list):
        #     if a in friends_set:
        #         friends_list[i].add(b)
        #         check = False
        #         break
        #     if b in friends_set:
        #         friends_list[i].add(a)
        #         check = False
        #         break
        # if check:
        #     friends_list.append({a, b})
    # group_num = len(friends_list)
    # max = 0
    # for friends_set in friends_list:
    #     length = len(friends_set)
    #     if length > max:
    #         max = length
    print(numnum)
    print(max(numnum.values()))


if __name__ == '__main__':
    main()
