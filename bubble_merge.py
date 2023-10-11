# Merges sort and another sorting algorithm will be used to sort everything. I like merge because it can split everything into smaller pieces. Then when it comes back together it should connect and be sorted. I will combine mergeSort and bubble sort


# Python program for implementation of Bubble Sort
import time
import string
import random

def bubbleSort(arr):
    n = len(arr)
   
    swapped = False

    for i in range(n-1):

        for j in range(0, n-i-1):
 
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
          
            return

def bubble_merge(myList):
  # It takes the list and splits it into two
    if len(myList) > 1:
      mid = len(myList) // 2
      left = myList[:mid]
      right = myList[mid:]
      # print(left)

  # After it splits it bubble sorts the splited list. Then at the end it bubble sorts the merged list bubble sorted list
      
      bubbleSort(left)
      # print(left)
      # print()
      # print(right)
      bubbleSort(right)
      # print(right)
      filler = left + right
      # print(filler)
      bubbleSort(filler)
      
      myList = filler
      return myList


# Test Section

arr = [12, 11, 13, 5, 6, 1, 600, -5, 22, 0 ]
arr1 = [9,8,7,6,5,4,3,2,1]
arr2 = [4,876,12,-4,12,7,421,-65]
arr3 = [1,5,2,8,-1,8,7,-66]
arr4 = [21,12]
arr5 = [2,4,0,1,3,44,7,88,-1,-44]
arr6 = [3,1,9,-2,-4,33,-21]
arr7 = [4,7,-1,-3,8,99,-99,11,1,0]

print("First array")
print(arr)
arr = bubble_merge(arr)
print(arr)

print()
print("Second array")
print(arr1)
arr1 = bubble_merge(arr1)
print(arr1)

print()
print("Third array")
print(arr2)
arr2 = bubble_merge(arr2)
print(arr2)

print()
print("Fourth array")
print(arr3)
arr3 = bubble_merge(arr3)
print(arr3)

print()
print("Fifth array")
print(arr4)
arr4 = bubble_merge(arr4)
print(arr4)

print()
print("Sixth array")
print(arr5)
arr5 = bubble_merge(arr5)
print(arr5)

print()
print("Seventh array")
print(arr6)
arr6 = bubble_merge(arr6)
print(arr6)

# TEST 1
print()
print("Test 1")
start1 = time.time_ns()
bubble_merge(arr7)
end1 = time.time_ns()
print("The run time of the bubble_merge: " + str(end1-start1))
print()

#TEST 2
print("Test 2")
start2 = time.time_ns()
bubble_merge(arr6)
end2 = time.time_ns()
print("The run time of the bubble_merge: " + str(end2-start2))

#TEST 3
print()
print("Test 3")
start3 = time.time_ns()
bubble_merge(arr5)
end3 = time.time_ns()
print("The run time of the bubble_merge: " + str(end3-start3))

#TEST 4
print()
print("Test 4")
start4 = time.time_ns()
bubble_merge(arr4)
end4 = time.time_ns()
print("The run time of the bubble_merge: " + str(end4-start4))

