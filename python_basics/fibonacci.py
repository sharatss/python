def fibonacci(n):
    old, new = 0, 1
    for i in range(0, n):
        if n <= 1:
            next = i
        else:
            next = old + new
            old = new
            new = next
        print(new)

n = input("Provide the value of n: ")
fibonacci(n)
