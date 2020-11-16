# -*- coding: utf-8 -*-
def cout_dif(a, b):
    sum = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            sum += 1
    return sum
    
def main():
    s = input()
    t = input()
    min = 10**5
    for i in range(len(s)-len(t)+1):
        sum = cout_dif(t, s[i:i+len(t)])
        if sum < min:
            min = sum
    print(min)

if __name__ == '__main__':
    main()
