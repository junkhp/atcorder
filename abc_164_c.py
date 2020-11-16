# -*- coding: utf-8 -*-

def main():
    n = int(input())
    keihin_set = set()
    for i in range(n):
        s = input()
        if not s in keihin_set:
            keihin_set.add(s)
    print(len(keihin_set))


if __name__ == "__main__":
    main()
