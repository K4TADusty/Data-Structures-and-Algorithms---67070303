"""Labs 05.03 - isIntersect(A, B, C)"""
def isIntersect(a, b, c):
    for item in a:
        if item in b and item in c:
            return True
    return False

if __name__ == "__main__":
    a = list(map(int, input().strip('[]').split(', ')))
    b = list(map(int, input().strip('[]').split(', ')))
    c = list(map(int, input().strip('[]').split(', ')))
    print(isIntersect(a, b, c))
