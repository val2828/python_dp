import sys
import math
import heapq

def check_if_sorted(main_arr, sorted_arr):
    main_arr  = sorted(main_arr)
    if main_arr == sorted_arr:
        print('Sorted correctly')
    else:
        print('Incorrect sorting')
#  the most basic sorting , we compare each item to be inserted with all the previous ones
#  for optimization can use only whiles or deque
# can reverse through reversed() or rewrite with whiles
def insertion_sort(in_arr):
    arr = list(in_arr)
    for i in range(1, len(arr)):
        for j in range(i):
                if arr[i] < arr[j]:
                    el = arr.pop(i)
                    arr = arr[:j] + [el] + arr[j:]
                    break
    return arr

#   this is the two methods for merge sort
# merge function simply
def merge(l1 ,l2):
    result = []
    while(l1 and l2):
        if l1[0] > l2[0]:
            el = l2.pop(0)
        else:
            el = l1.pop(0)
        result.append(el)

    while(l1):
        result.append(l1.pop(0))

    while (l2):
        result.append(l2.pop(0))

    return result

def merge_sort(arr):
    if len(arr) ==1:
       return arr

    ls1 = arr[:len(arr)//2]
    ls2 = arr[len(arr)//2:]

    ls1 = merge_sort(ls1)
    ls2 = merge_sort(ls2)

    return merge(ls1, ls2)

def merge_index(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    left = arr[p:p+n1]
    right = arr[q+1:q+1+n2]

    left += [sys.maxsize]
    right += [sys.maxsize]

    i = 0
    j = 0

    for k in range(p,r+1):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
def merge_sort_index(arr, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort_index(arr, p , q)
        merge_sort_index(arr, q+1, r)
        merge_index(arr, p, q, r)


class MaxHeap():

    def __init__(self, ls):
        self.heap_arr = ls
        self.heap_len = len(ls)
        self.heap_size = len(ls)


def max_heapify(heap, i):
    left = 2*i + 1
    right = 2*i + 2

    if left < heap.heap_size and heap.heap_arr[left] > heap.heap_arr[i]:
            largest = left
    else:
        largest = i
    if right < heap.heap_size and heap.heap_arr[right] > heap.heap_arr[largest]:
            largest = right
    if largest != i:
        heap.heap_arr[i], heap.heap_arr[largest] = heap.heap_arr[largest], heap.heap_arr[i]
        max_heapify(heap, largest)

def build_max_heap(heap):
    for i in reversed(range(heap.heap_len//2)):
        max_heapify(heap, i)

def heap_sort(arr):
    heap = MaxHeap(arr)
    build_max_heap(heap)
    print(heap.heap_arr)
    for i in reversed(range(1, heap.heap_len)):
        heap.heap_arr[0], heap.heap_arr[i] = heap.heap_arr[i], heap.heap_arr[0]
        heap.heap_size -= 1
        max_heapify(heap, 0)


if __name__ == '__main__':
    ## len is 10
    unsorted_arr  = [2, 1, 3, 4, 1, 7, 4 , 6, 5, 8]
    unsorted_arr_for_heapq = [2, 1, 3, 4, 1, 7, 4, 6, 5, 8]
    heapq._heapify_max(unsorted_arr_for_heapq)
    print(unsorted_arr_for_heapq)
    # unsorted_arr  = [5,4,5,3,2,1]
    # print(unsorted_arr)
    # sorted_arr = merge_sort_index(unsorted_arr, 0, len(unsorted_arr)-1)
    #
    # print(unsorted_arr)
    # print(sorted_arr)
    #
    # check_if_sorted(unsorted_arr, sorted_arr)
    heap_sort(unsorted_arr)
    print(unsorted_arr)