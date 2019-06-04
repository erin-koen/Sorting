import math
# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []
    # TO-DO
    while len(arrA) > 0 or len(arrB) > 0:
        if len(arrA) > 0 and len(arrB) > 0:
            if arrA[0] < arrB[0]:
                merged_arr.append(arrA.pop(0))
            else:
                merged_arr.append(arrB.pop(0))
        elif len(arrA) > 0:
            merged_arr.append(arrA.pop(0))
        elif len(arrB) > 0:
            merged_arr.append(arrB.pop(0))
    
    print('merge', merged_arr)        

    return merged_arr




# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # break down the array into component parts until they hit 1, then start combining them using merge(). Recursion for breakdown controlled by length of array
    if len(arr)<=1:
        return arr 
    
    midpoint = math.floor(len(arr)/2)
    leftArr = arr[0:midpoint]
    rightArr = arr[midpoint:]

    print('left', leftArr)
    print('right', rightArr)

    L = merge_sort(leftArr)
    R = merge_sort(rightArr)

    arr = merge(L, R)


    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
