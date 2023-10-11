
# Python program for implementation of Bubble Sort
#Code gotten from geekforgeeks.org

import time
import string
import random

def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we 
            # can just exit the main loop.
            return
 
 


def insertionSort(arr):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position



# Python program for implementation of Quicksort Sort
 
# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot
 
 
# Function to find the partition position
def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
 
 
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
 
# Driver code to test above
arr = [12, 11, 13, 5, 6, 1, 600, -5, 22, 0 ]
arr1 = [9,8,7,6,5,4,3,2,1]
arr2 = [4,876,12,-4,12,7,421,-65]
arr3 = [1,5,2,8,-1,8,7,-66]
arr4 = [21,12]
arr5 = [2,4,0,1,3,44,7,88,-1,-44]
arr6 = [3,1,9,-2,-4,33,-21]
arr7 = [4,7,-1,-3,8,99,-99,11,1,0]

n7 = len(arr7)
n6 = len(arr6)
n5 = len(arr5)
n4 = len(arr4)



# TEST 1
print("Test 1")
start1 = time.time_ns()
mergeSort(arr7, 0, n7-1)
end1 = time.time_ns()
print("The run time of the Merge sort is: " + str(end1-start1))

start2 = time.time_ns()
quickSort(arr7, 0, n7-1)
end2 = time.time_ns()
print("The run time of the Quick sort is: " + str(end2-start2))

start3 = time.time_ns()
insertionSort(arr7)
end3 = time.time_ns()
print("The run time of the Insertion sort  is: " + str(end3-start3))

start4 = time.time_ns()
bubbleSort(arr7)
end4 = time.time_ns()
print("The run time of the Bubble sort  is: " + str(end4-start4))
print()
#TEST 2
print("Test 2")
start5 = time.time_ns()
mergeSort(arr6, 0, n6-1)
end5 = time.time_ns()
print("The run time of the Merge sort is: " + str(end5-start5))

start6 = time.time_ns()
quickSort(arr6, 0, n6-1)
end6 = time.time_ns()
print("The run time of the Quick sort is: " + str(end6-start6))

start7 = time.time_ns()
insertionSort(arr6)
end7 = time.time_ns()
print("The run time of the Insertion sort  is: " + str(end7-start7))

start8 = time.time_ns()
bubbleSort(arr6)
end8 = time.time_ns()
print("The run time of the Bubble sort  is: " + str(end8-start8))
print()
#TEST 3
print("Test 3")
start9 = time.time_ns()
mergeSort(arr5, 0, n5-1)
end9 = time.time_ns()
print("The run time of the Merge sort is: " + str(end9-start9))

start10 = time.time_ns()
quickSort(arr5, 0, n5-1)
end10 = time.time_ns()
print("The run time of the Quick sort is: " + str(end10-start10))

start11 = time.time_ns()
insertionSort(arr5)
end11 = time.time_ns()
print("The run time of the Insertion sort  is: " + str(end11-start11))

start12 = time.time_ns()
bubbleSort(arr5)
end12 = time.time_ns()
print("The run time of the Bubble sort  is: " + str(end12-start12))
print()
#TEST 4
print("Test 4")
start13 = time.time_ns()
mergeSort(arr4, 0, n4-1)
end13 = time.time_ns()
print("The run time of the Merge sort is: " + str(end13-start13))

start14 = time.time_ns()
quickSort(arr4, 0, n4-1)
end14 = time.time_ns()
print("The run time of the Quick sort is: " + str(end14-start14))

start15 = time.time_ns()
insertionSort(arr4)
end15 = time.time_ns()
print("The run time of the Insertion sort  is: " + str(end15-start15))

start16 = time.time_ns()
bubbleSort(arr4)
end16= time.time_ns()
print("The run time of the Bubble sort  is: " + str(end16-start16))
