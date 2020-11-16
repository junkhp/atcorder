# -*- coding: utf-8 -*-

def num2alpha(num):
    if num <= 26:
        return chr(64+num)
    elif num % 26 == 0:
        return num2alpha(num//26-1)+chr(90)
    else:
        return num2alpha(num // 26) + chr(64 + num % 26)


def base_10_to_n(X, n):
    if (int(X/n)):
        return base_10_to_n(int(X/n), n)+str(X % n)
    return str(X % n)


def main():
    n = int(input())
    alpha = num2alpha(n)
    print(alpha.lower())


if __name__ == "__main__":
    main()
