def fibonacci(n):
    start = 0
    second = 1
    for i in range(n):
        print(start)
        start, second = second, start + second

fibonacci(10)