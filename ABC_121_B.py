# -*- coding: utf-8 -*-
def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        sum = 0
        A = list(map(int, input().split()))
        for j in range(M):
            sum += A[j]*B[j]
        # print(sum+C)
        if sum + C > 0:
            cnt += 1
    print(cnt)
if __name__ == '__main__':
    main()
