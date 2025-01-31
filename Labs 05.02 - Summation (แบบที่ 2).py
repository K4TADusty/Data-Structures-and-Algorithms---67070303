def formula(n):
    sum_n = 0
    for i in range(n + 1):
        sum_n += i
    return sum_n

if __name__ == "__main__":
    n = int(input())
    print(formula(n))
