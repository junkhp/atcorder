import math


def main():
    n = int(input())
    sum = (n-1)*2-1
    for i in range(2, n):
        sho = n // i
        amari = n % i
        if i**2 >= n:
            break
        if amari == 0:
            sho -= 1
        sum += (sho - i+1) * 2 - 1
    print(sum)


if __name__ == "__main__":
    main()
