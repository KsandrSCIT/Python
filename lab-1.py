target = int(input())
arr = [1, 5, 9, 7, 3, 5]
flag = True

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] + arr[j] == target and flag:
            print(i, j)
            flag = False


