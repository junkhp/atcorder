# -*- coding: utf-8 -*-


def main():
    n = int(input())
    ab_list = [list(map(int, input().split())) for i in range(n)]
    score = 0
    for ab in ab_list:
        score += ab[0]

    score_list = sorted([2 * ab[0] + ab[1] for ab in ab_list], reverse=True)
    my_score = 0
    ans = 0

    for i, plus_score in enumerate(score_list):
        if my_score > score:
            break
        my_score += plus_score
    if i == 0:
        i += 1
    print(i)
    
if __name__ == '__main__':
    main()