from Selection_sort import selection_sort
from Merge_sort import merge_sort
from Insertion_sort import insertion_sort
from Shell_sort import shellsort
from Arrays import create_descending,create_ascending,create_123,create_random_array
import random
import time
from copy import deepcopy
import matplotlib.pyplot as plt
import numpy as np


def time_comparison(array):

    copy1 = deepcopy(array)
    copy2 = deepcopy(array)
    copy3 = deepcopy(array)
    copy4 = deepcopy(array)

    start1 = time.perf_counter()
    insertion_sort(copy1)
    finish1 = time.perf_counter()
    time_insert = finish1 - start1
    
    start2 = time.perf_counter()
    selection_sort(copy2)
    finish2 = time.perf_counter()
    selection_time = finish2 - start2
    
    start3 = time.perf_counter()
    merge_sort(copy3)
    finish3 = time.perf_counter()
    merge_time = finish3 - start3
    
    start4 = time.perf_counter()
    shellsort(copy4)
    finish4 = time.perf_counter()
    shell_time = finish4 - start4

    return time_insert, selection_time,merge_time,shell_time


def main_time():
    insertion_time_random = []
    insertion_time_ascending = []
    insertion_time_descending = []
    insertion_time_123 = []

    select_time_random = []
    select_time_ascending = []
    select_time_descending = []
    select_time_123 = []

    merge_time_random = []
    merge_time_ascending = []
    merge_time_descending = []
    merge_time_123 = []

    shell_time_random = []
    shell_time_ascending = []
    shell_time_descending = []
    shell_time_123 = []

    for i in range(9):
        array_size = 2**(7+i)

        random_array = create_random_array(array_size)
        ascending_array = create_ascending(array_size)
        descending_array = create_descending(array_size)
        array_123 = create_123(array_size)

        output_random = time_comparison(random_array)
        insertion_time_random.append(output_random[0])
        select_time_random.append(output_random[1])
        merge_time_random.append(output_random[2])
        shell_time_random.append(output_random[3])

        output_ascending = time_comparison(ascending_array)
        insertion_time_ascending.append(output_ascending[0])
        select_time_ascending.append(output_ascending[1])
        merge_time_ascending.append(output_ascending[2])
        shell_time_ascending.append(output_ascending[3])

        output_descending = time_comparison(descending_array)
        insertion_time_descending.append(output_descending[0])
        select_time_descending.append(output_descending[1])
        merge_time_descending.append(output_descending[2])
        shell_time_descending.append(output_descending[3])

        output_123 = time_comparison(array_123)
        insertion_time_123.append(output_123[0])
        select_time_123.append(output_123[1])
        merge_time_123.append(output_123[2])
        shell_time_123.append(output_123[3])
    
    return insertion_time_random,select_time_random,merge_time_random,shell_time_random, \
    insertion_time_ascending,select_time_ascending,merge_time_ascending,shell_time_ascending, \
    insertion_time_descending,select_time_descending,merge_time_descending,shell_time_descending, \
    insertion_time_123,select_time_123,merge_time_123,shell_time_123


def number_of_comparisons(array):
    copy1 = deepcopy(array)
    copy2 = deepcopy(array)
    copy3 = deepcopy(array)
    copy4 = deepcopy(array)

    insert_comp = insertion_sort(copy1)[1]
    select_comp = selection_sort(copy2)[1]
    merge_comp = merge_sort(copy3)
    shell_comp = shellsort(copy4)[1]

    return insert_comp,select_comp,merge_comp,shell_comp


def main_comparisons():
    insertion_comps_random = []
    insertion_comps_ascending = []
    insertion_comps_descending = []
    insertion_comps_123 = []

    select_comps_random = []
    select_comps_ascending = []
    select_comps_descending = []
    select_comps_123 = []

    merge_comps_random = []
    merge_comps_ascending = []
    merge_comps_descending = []
    merge_comps_123 = []

    shell_comps_random = []
    shell_comps_ascending = []
    shell_comps_descending = []
    shell_comps_123 = []

    for i in range(9):
        array_size = 2**(7+i)

        random_array = create_random_array(array_size)
        ascending_array = create_ascending(array_size)
        descending_array = create_descending(array_size)
        array_123 = create_123(array_size)

        output_random = number_of_comparisons(random_array)
        insertion_comps_random.append(output_random[0])
        select_comps_random.append(output_random[1])
        merge_comps_random.append(output_random[2])
        shell_comps_random.append(output_random[3])

        output_ascending = number_of_comparisons(ascending_array)
        insertion_comps_ascending.append(output_ascending[0])
        select_comps_ascending.append(output_ascending[1])
        merge_comps_ascending.append(output_ascending[2])
        shell_comps_ascending.append(output_ascending[3])

        output_descending = number_of_comparisons(descending_array)
        insertion_comps_descending.append(output_descending[0])
        select_comps_descending.append(output_descending[1])
        merge_comps_descending.append(output_descending[2])
        shell_comps_descending.append(output_descending[3])

        output_123 = number_of_comparisons(array_123)
        insertion_comps_123.append(output_123[0])
        select_comps_123.append(output_123[1])
        merge_comps_123.append(output_123[2])
        shell_comps_123.append(output_123[3])

    return insertion_comps_random,select_comps_random,merge_comps_random,shell_comps_random,\
        insertion_comps_ascending,select_comps_ascending,merge_comps_ascending,shell_comps_ascending,\
        insertion_comps_descending,select_comps_descending,merge_comps_descending,shell_comps_descending,\
        insertion_comps_123,select_comps_123,merge_comps_123,shell_comps_123



def graph(array):
    plt.yscale("log")
    plt.plot([7,8,9,10,11,12,13,14,15],array[0])
    plt.plot([7,8,9,10,11,12,13,14,15],array[1])
    plt.plot([7,8,9,10,11,12,13,14,15],array[2])
    plt.plot([7,8,9,10,11,12,13,14,15],array[3])
    plt.show()

    plt.yscale("log")
    plt.plot([7,8,9,10,11,12,13,14,15],array[4])
    plt.plot([7,8,9,10,11,12,13,14,15],array[5])
    plt.plot([7,8,9,10,11,12,13,14,15],array[6])
    plt.plot([7,8,9,10,11,12,13,14,15],array[7])
    plt.show()

    plt.yscale("log")
    plt.plot([7,8,9,10,11,12,13,14,15],array[8])
    plt.plot([7,8,9,10,11,12,13,14,15],array[9])
    plt.plot([7,8,9,10,11,12,13,14,15],array[10])
    plt.plot([7,8,9,10,11,12,13,14,15],array[11])
    plt.show()

    plt.yscale("log")
    plt.plot([7,8,9,10,11,12,13,14,15],array[12])
    plt.plot([7,8,9,10,11,12,13,14,15],array[13])
    plt.plot([7,8,9,10,11,12,13,14,15],array[14])
    plt.plot([7,8,9,10,11,12,13,14,15],array[15])
    plt.show()
        

def main():
    # graph(main_time())
    graph(main_comparisons())

main()