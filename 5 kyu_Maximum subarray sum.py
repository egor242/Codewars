def max_sequence(arr):
    best_sum = current_sum = 0
    for num in arr:
        current_sum = max(0, current_sum + num)
        best_sum = max(current_sum, best_sum)
    return best_sum


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))