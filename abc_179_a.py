def main():
    n = input()
    if n[-1] == 's':
        ans = n + 'es'
    else:
        ans = n+'s'
    print(ans)


if __name__ == "__main__":
    main()
