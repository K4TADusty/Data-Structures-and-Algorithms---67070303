"""Labs 05.01 - Summation (แบบที่ 1)"""
def loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

if __name__ == "__main__":
    n = int(input())
    print(loop(n))
