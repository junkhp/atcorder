# -*- coding: utf-8 -*-
def main():
    N = int(input())
    A = list(map(int, input().split()))
    adict = {}
    for a in A:
        if a in adict.keys():
            adict[a] += 1
        else:
            adict[a] = 1
    # print(adict)
    sum = 0
    for key, v in adict.items():
        sum += key*v
    # print(sum)
    Q = int(input())
    for i in range(Q):
        B, C = map(int, input().split())
        keys_ = adict.keys()
        if B in keys_ and C in keys_:
            sum = sum - B*adict[B] + C*adict[B]
            adict[C] += adict[B]
            adict[B] = 0
        elif B in keys_:
            sum = sum - B*adict[B] + C*adict[B]
            adict[C] = adict[B]
            adict[B] = 0
        print(sum)

if __name__ == '__main__':
    main()
