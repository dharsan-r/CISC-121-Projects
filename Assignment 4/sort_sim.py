""""
Author: Dharsan Ravindran
Student ID: 20219218
Date: April 10, 2021
Instructor: Professor Burton Ma
"""


import random
import time
import a4


def time_to_sort(sorter, t):
    '''
    Returns the times needed to sort lists of sizes sz = [1024, 2048, 4096, 8192]
    
    The function sorts the slice t[0:sz] using the sorting function
    specified by the caller and records the time required in seconds.
    Because a slice is sorted instead of the list t, the list t is not modified by
    this function. The list t should have at least 8192 elements.

    The times are returned in a list of length 4 where the times in seconds
    are formatted strings having 4 digits after the decimal point making it easier to
    print the returned lists.

    Parameters
    ----------
    sorter : function
             A sorting function from the module a4.
    t : list of comparable type
        A list of elements to slice and sort.

    Returns
    -------
    list of str
        The times to sort lists of lengths 1024, 2048, 4096, and 8192.

    Raises
    ------
    ValueError
        If len(t) is less than 8192.
    '''

    if len(t) < 8192:
        raise ValueError('not enough elements in t')
    times = []
    for sz in [1024, 2048, 4096, 8192]:
        # slice t
        u = t[0:sz]
        # record the time needed to sort
        tic = time.perf_counter()
        sorter(u)
        toc = time.perf_counter()
        times.append(f'{toc - tic:0.4f}')
    return times


def get_times(t):
    times = time_to_sort(a4.selection_sort, t)
    print(times, "selection sort")
    times = time_to_sort(a4.insertion_sort, t)
    print(times, "insertion sort 1")
    times = time_to_sort(a4.insertion_sort2, t)
    print(times, "insertion sort 2")
    times = time_to_sort(a4.merge_sort, t)
    print(times, "merge sort")


def sim_sorted():
    n = 8192
    t = list(range(n))
    get_times(t)


def sim_partial():
    n = 8192
    t = list(range(n))
    a4.partial_shuffle(t)
    get_times(t)


def sim_reverse():
    n = 8192
    t = list(range(n))
    t.reverse()
    get_times(t)


def sim_shuffled():
    n = 8192
    t = list(range(n))
    random.shuffle(t)
    get_times(t)
