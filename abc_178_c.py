from scipy.special import comb
def main():
    n = int(input())
    # sum = 0
    # for i in range(1, n):
    #     sum += comb(n, i, exact=True)
    # sub = (n-2)*sum
    # ans = n*(n-1)*(10**(n-2))-sub
    ans = 10**n - 2*(9**n) + 8**n
    print(int(ans%((10)**9+7)))
if __name__ == '__main__':
    main()
