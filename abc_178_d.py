from scipy.special import comb
# ここがうまくできるととける
def bunkatusu(s, k):
    return (s+1)**(k-1)
    # return comb(s-1, k-1, exact=True)

def main():
    # s = int(input())
    s = 16
    syo = s//3
    amari = s%3
    sum = 0
    for i in range(2, syo+1):
        print(i, end=':')
        print(bunkatusu(s-i*3, i))
        sum += bunkatusu(s-i*3, i)
    print((sum+1)%(10**9+7))

if __name__ == '__main__':
    main()
