# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    counter = 0
    while len(arrA) and len(arrB):
        if arrA[0] < arrB[0]:
            merged_arr[counter] = arrA.pop(0)
            counter += 1
        else:
            merged_arr[counter] = arrB.pop(0)
            counter += 1
    
    while len(arrA):
        merged_arr[counter] = arrA.pop(0)
        counter += 1
    
    while len(arrB):
        merged_arr[counter] = arrB.pop(0)
        counter += 1

    return merged_arr


print('merge test', merge([1,3,5,7],[2,4,6,8]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO


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
