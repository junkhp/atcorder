# -*- coding: utf-8 -*-
def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    h_dict = {}
    for i in range(len(h)):
        h_dict[i+1] = h[i]
    out = []
    for k in range(m):
        a, b = map(int, input().split())
        ha = h_dict[a]
        hb = h_dict[b]
        if ha > hb:
            out.append(b)
        elif ha < hb:
            out.append(a)
        else:
            out.append(a)
            out.append(b)
    out = set(out)
    print(n - len(out))
if __name__ == '__main__':
    main()
