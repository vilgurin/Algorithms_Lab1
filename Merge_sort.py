counter =0
def merge_sort(array):
    comps = 0
    if len(array) > 1:
        mid = len(array)//2
        l = array[:mid]
        r = array[mid:]
        merge_sort(l)
        merge_sort(r)
        comps += l[0]+r[0]
        i = j = k = 0
        while i < len(l) and j < len(r):
            comps += 1
            if l[i] < r[j]:
                array[k] = l[i]
                i += 1
            else:
                array[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1
            comps += 1
        while j < len(r):
            array[k] = r[j]
            j += 1
            k += 1
            comps += 1
    return comps
    