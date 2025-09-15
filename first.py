def factorial(n):
    if n == 0:
        return 1                
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def print_string():
    return "conflict test"

def print_series(n):
    series = []
    for i in range(1, n + 1):
        series.append(i * (i + 1) // 2)
    return series

def main():
    print(factorial(10))
    print(print_string())
    print(print_series(10))

if __name__ == "__main__":
    main()