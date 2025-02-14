"""Labs 07.01 - Insertion Sort"""

def insertionSort():
    lst = list(map(int, input().strip('[]').split(', ')))
    last = int(input())
    comparisons = 0
    for i in range(1, last + 1):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            comparisons += 1
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
        comparisons += 1 if j >= 0 else 0
        print(lst)
    print(f"Comparison times: {comparisons}")
insertionSort()
