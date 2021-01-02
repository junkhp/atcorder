# -*- coding: utf-8 -*-
from itertools import accumulate

def can_make(s, num_dict):
    for num in num_dict.keys():
        if num_dict[num] > s[num]:
            return False
    return True

    


def make_dict(s):
    num_dict = {}
    num_list = list(map(int, list(str(s))))
    if len(num_list) == 1:
        num_list = [0, 0, 8]
    elif len(num_list) == 2:
        num_list.append(0)
    
    for num in num_list:
        try:
            num_dict[num] += 1
        except KeyError:
            num_dict[num] = 1
        
        return num_dict


def main():
    s = input()
    original_num = int(s)
    s_list = list(map(int, list(s)))
    s_dict = {}
    for i in range(10):
        s_dict[i] = 0
    for s in s_list:
        s_dict[s] += 1


    for i in range(8, 1000, 8):
        if can_make(s_dict, make_dict(i)):
            print('Yes')
            return
    print('No')

if __name__ == "__main__":
    main()
