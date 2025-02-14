"""Labs 07.02 - Selection Sort"""

def selectionSort():
    lst = list(map(int, input().strip('[]').split(', ')))
    last = int(input())
    comparisons = 0
    for i in range(last):
        min_index = i
        for j in range(i + 1, last + 1):
            comparisons += 1
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
        print(lst)
    print(f"Comparison times: {comparisons}")
selectionSort()
