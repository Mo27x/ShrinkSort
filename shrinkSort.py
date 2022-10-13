def shrink_sort(arr):
    start, end = 0, len(arr)
    while end - start > 1:
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
        start += 1
        end -= 1
    return arr
