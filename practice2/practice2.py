def fib(n):
    fibonacci = [0] * (n+1)

    def _fib(n):
        if n == 1:
            return 1
        elif n == 2:
            return 1
        elif fibonacci[n] != 0:
            return fibonacci[n]
        else:
            fibonacci[n] = _fib(n-1) + _fib(n-2)
            return fibonacci[n]

    return _fib(n)


print("数値を入力してください: ", end="")
i = int(input())
print("フィボナッチ数列の第" + str(i) + "項は" + str(fib(i)) + "です。")
