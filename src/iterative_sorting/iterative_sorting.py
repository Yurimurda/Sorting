import random
arr = list(range(10))
random.shuffle(arr)
print(arr)
# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]



    return arr
    


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    sorted_elems = 0
    while sorted_elems != len(arr):
        for i in range(len(arr) - sorted_elems - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        sorted_elems += 1
    return arr

print (bubble_sort(arr))
print(selection_sort(arr))
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

