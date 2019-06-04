import math
# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    arrA_counter = 0
    arrB_counter = 0
    merged_arr_counter = 0

    while arrA_counter < len(arrA) and arrB_counter < len(arrB):
        if arrA[arrA_counter] < arrB[arrB_counter]:
            merged_arr[merged_arr_counter] = arrA[arrA_counter]
            print('a', merged_arr)
            arrA_counter += 1
            merged_arr_counter += 1
        else:
            merged_arr[merged_arr_counter] = arrA[arrB_counter]
            print('b', merged_arr)
            
            arrB_counter += 1
            merged_arr_counter += 1
    
    while arrA_counter < len(arrA):
        merged_arr[merged_arr_counter] = arrA[arrA_counter]
        arrA_counter += 1
        merged_arr_counter += 1
    
    while arrB_counter < len(arrB):
        merged_arr[merged_arr_counter] = arrB[arrB_counter]
        arrB_counter += 1
        merged_arr_counter += 1

    return merged_arr


print('merge test ', merge([1,5,9,3,55],[2]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # break down the array into component parts until they hit 1, then start combining them using merge(). Recursion for breakdown controlled by length of array
    if len(arr)==1:
        return
    
    midpoint = math.floor(len(arr)/2)
    leftArr = arr[0:midpoint]
    rightArr = arr[midpoint:]

    print('left', leftArr)
    print('right', rightArr)

    merge_sort(leftArr)
    merge_sort(rightArr)

   


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
