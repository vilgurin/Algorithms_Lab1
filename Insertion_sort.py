def insertion_sort(array):
    counter = 0
    for i in range(1,len(array)):
        current = array[i]
        j = i-1
        counter += 1
        while current < array[j] and j>=0:
            counter += 1
            array[j],array[i] = current,array[j]
            j -= 1
            i -= 1
    return array,counter