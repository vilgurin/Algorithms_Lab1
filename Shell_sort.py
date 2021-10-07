def shellsort(arr):
    counter = 0
    n = len(arr)
    gap = int(n/2)

    while gap > 0:

        for i in range(gap, n):
            elem = arr[i]
            j = i

            while j >= gap and arr[j - gap] > elem:
                counter += 1
                arr[j] = arr[j - gap]
                j -= gap

            counter += 1
            arr[j] = elem

        gap //= 2

    return arr, counter