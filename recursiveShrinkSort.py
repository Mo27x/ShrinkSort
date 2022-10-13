def recursive_shrink_sort(arr, start, end):
    if end - start <= 1:
        return arr
    min, max = start, end - 1
    for i in range(start, end):
        if arr[i] <= arr[min]:
            min = i
        if arr[i] >= arr[max]:
            max = i
    tmp = arr[start]
    arr[start] = arr[min]
    arr[min] = tmp
    if max == start:
        max = min
    tmp = arr[end - 1]
    arr[end - 1] = arr[max]
    arr[max] = tmp
    return recursive_shrink_sort(arr, start + 1, end - 1)