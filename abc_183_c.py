# -*- coding: utf-8 -*-
from itertools import permutations
def main():
    n, k = map(int, input().split())
    t_list = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    for junban in permutations(range(n - 1)):
        junban = list(junban)
        junban.append(n-1)
        all_time = 0
        for i in range(1, n):
            if all_time <= k:
                prev_city = junban[i-1]
                city = junban[i]
                time = t_list[prev_city][city]
                all_time += time
            else:
                break

        all_time += t_list[junban[-1]][junban[0]]
        if all_time == k:
            ans += 1
    
    print(ans)
        



if __name__ == '__main__':
    main()
