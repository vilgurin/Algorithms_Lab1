def selection_sort(array):

    counter = 0
    for i in range(len(array)):
        min_i = i
        for j in range(i+1,len(array)):
            counter += 1
            if array[j] < array[min_i]:
                min_i = j
        array[i],array[min_i] = array[min_i],array[i]
    return array,counter