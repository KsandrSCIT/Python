# target = 6
# arr = [3,2,4]
def summ_two_numbers (target,arr):

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]


# summ_two_numbers(target, arr)