def main():
     n, x, t = map(int, input().split())
     if n % x == 0:
         ans = n/x*t
     else:
         ans = (n//x+1)*t
     print(int(ans))

if __name__ == '__main__':
    main()
