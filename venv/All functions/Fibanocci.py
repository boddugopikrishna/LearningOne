def fibanocci(n):
        fib = {}
        for k in range(0,n+1):
            if k == 0:
                fib[k] = 0
            elif k >= 1 and k <= 2:
                fib[k] = 1
            else:
                fib[k] = fib[k - 1] + fib [k - 2]
        return fib[n]
print(fibanocci(100))