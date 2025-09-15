def factorial(n):
    if n == 0:
        return 1                
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def print_string():
    return "I am Ashik. This line is mine."

def main():
    print(factorial(10))
    print(print_string())

if __name__ == "__main__":
    main()