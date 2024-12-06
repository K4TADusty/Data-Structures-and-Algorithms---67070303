"""Lab 01.01 - Is_Even"""
def is_even(a):
    if a & 1 ==0:
        print(True)
    else:
        print(False)
is_even(int(input()))