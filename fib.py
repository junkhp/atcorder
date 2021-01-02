# -*- coding: utf-8 -*-
import time
def fib(n):
    if n == 0 or n == 1:
        return 1

    return fib(n-1) + fib(n - 2)


class FibMemo:
    def __init__(self):
        self.fib_memo = {}

    def cal_fib(self, n):
        if n == 0 or n == 1:
            self.fib_memo[n] = 1

        if n in self.fib_memo.keys():
            return self.fib_memo[n]
        
        self.fib_memo[n] = self.cal_fib(n - 1) + self.cal_fib(n - 2)
        return self.fib_memo[n]


def fib_dp(n):
    cal_result = {}
    cal_result[0] = 1
    cal_result[1] = 1

    if n == 0 or n == 1:
        return 1

    for i in range(2, n + 1):
        cal_result[i] = cal_result[i - 1] + cal_result[i - 2]
    return cal_result[n]


if __name__ == "__main__":
    n = 10
    print(fib(n))

    print(fib_dp(n))

    fibmemo1 = FibMemo()
    print(fibmemo1.cal_fib(n))