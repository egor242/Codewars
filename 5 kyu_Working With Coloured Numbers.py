"""
def same_col_seq(val, k, col):
    # your code here
    return []
"""


def check_colour(n):
    if not ((n - 1) % 3):
        return "red"
    if not ((n - 2) % 3):
        return "yellow"
    if not ((n - 3) % 3):
        return "blue"


def same_col_seq(val, k, col):
    arr = []
    i = 1
    elem = 0

    while elem < 2 * k * val:
        elem = sum(range(i+1))
        if elem > val:
            if check_colour(elem) == col:
                if len(arr) < k:
                    arr.append(elem)
                else:
                    break
        i += 1
    return arr



print(same_col_seq(250, 6, "yellow"))