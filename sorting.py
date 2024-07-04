arr = [1, 6, 3, 5, 2, 4, 7, 0]

"""
Selection Sort:
    1. Find min element from i to n
    2. Swap with i th element
"""

def selection_sort(arr):
    print(f"Selection Sort on {arr}")
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"{i} : {arr}")
    
"""
Selecion Sort with recursion:
sel_sort(arr, i):
    Base case i == n: return
    1. Find min element from i to n
    2. Swap min and i element
    3. Sort remaining arr i.e sel_sort(arr, i+1)

Finding minimum also using recursion
find_min_index(arr, i):
    Base case: i == n: return n
    1. Find min for the rest of the array i.e find_min_index(arr, i+1)
    2. If arr[i] < min, 
        2a. then, return i
        2b. else, return min
"""
def find_min_index_rec(arr, i):
    if i == len(arr)-1:
        return i
    min_index = find_min_index_rec(arr, i+1)
    if arr[i] < arr[min_index]:
        return i
    return min_index


def selection_sort_rec(arr, i):
    if i == len(arr)-1:
        return
    min_index = find_min_index_rec(arr, i)
    arr[i], arr[min_index] = arr[min_index], arr[i]
    print(f"{i} : {arr}")
    selection_sort_rec(arr, i+1)


"""
Insertion Sort:
    1. Loop i = 0 to n-1
        1a. Loop j = i to 0, while arr[i] < arr[j] is true (Find the correct index for the i-th element in the sorted arr from (0 to i-1)) 
            1aa. move all elements from j+1 to i-1 by +1
            1ab. put our element in j+1 

v1
def insertion_sort(arr):
    n = len(arr)
    print(f"Insertion sort on {arr}")
    for i in range(0, n):
        current_element = arr[i]
        
        j = i-1
        while(j >=0 and arr[i] < arr[j]):
            j -= 1
        
        # Shifting
        for k in range(i-1, j, -1):
            arr[k+1] = arr[k]
        
        # Setting 
        arr[j+1] = current_element

        print(f"{i} : {arr}")
"""

def insertion_sort(arr):
    n = len(arr)
    print(f"Insertion sort on {arr}")
    for i in range(1, n):
        current_element = arr[i]
        j = i-1
        while(j >=0 and current_element < arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current_element
        print(f"{i} : {arr}")



"""
Merge Sort:

    Base Case 1: if size of arr = 1, then it is sorted
    Split arr into two
    Sort(first half)
    Sort(second half)
    merge(first half, second half)

"""

def merge(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    arr3 = [0] * (m+n)

    i = 0
    j = 0
    k = 0

    while(i < m and j < n):
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i += 1
        else:
            arr3[k] = arr2[j]
            j += 1
        k += 1
    
    while(i < m):
        arr3[k] = arr1[i]
        k += 1
        i += 1
    
    while(j < n):
        arr3[k] = arr2[j]
        j += 1
        k += 1

    return arr3

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    arr1 = arr[:mid]
    arr2 = arr[mid:]

    sorted_arr1 = merge_sort(arr1)
    sorted_arr2 = merge_sort(arr2)

    sorted_merged = merge(sorted_arr1, sorted_arr2)
    print(sorted_merged)
    return sorted_merged


def merge_inplace(arr, left, mid, right):
    temp_left = arr[left:mid]
    temp_right = arr[mid:right]

    m = len(temp_left)
    n = len(temp_right)

    i=0 
    j=0 
    k=left # this is important
    while(i < m and j < n):
        if temp_left[i] < temp_right[j]:
            arr[k] = temp_left[i]
            i += 1
        else:
            arr[k] = temp_right[j]
            j += 1
        k += 1
    
    while(i < m):
        arr[k] = temp_left[i]
        k += 1
        i += 1

    while(j < n):
        arr[k] = temp_right[j]
        k += 1
        j += 1


def merge_sort_inplace(arr, left, right):
    # Base case, only one element
    if left == right - 1:
        return 
    mid = (left+right) // 2
    merge_sort_inplace(arr, left, mid)
    merge_sort_inplace(arr, mid, right)
    merge_inplace(arr, left, mid, right)
    print(f"{left = } {right = } {mid  = } : {arr}")


