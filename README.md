CMPSC 463 Project 1 
Charles Langley

Research and Study

 Students will start by studying various sorting algorithms.

https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm 
In this site it talked about all the different sorting algorithms like merge sort and bubble sort. I thinking about choosing insertion sort and merge sort to see how they fair together.

https://realpython.com/sorting-algorithms-python/  
This site also talked further about the different sorting algorithms. It also talked about bubble sort and I want to now instead use bubble sort and merge sort instead of insertion sort because I believe bubble sort might be improved thanks to a merge sort implementation.
 https://www.geeksforgeeks.org/sorting-algorithms-in-python/ 
This site piggybacks off the other sites about the same sorting algorithms that I already mentioned.

https://www.geeksforgeeks.org/python-program-for-quicksort/ 
This site talks about the quick sort algorithm and I was thinking about using it but I decided to settle on merge sort and 



Algorithm Design
	For my algorithm design I combined elements from merge sort and elements from bubble sort to create bubble merge sort. It's pretty simple. It divides the list into two separate lists and then applies bubble sort. Then it recombines and then performs bubble sort one final time. I could experiment how many times I want to divide the list and see if that would improve the algorithm’s performance. I believe bubble sort fusion with merge sort is like the best of both worlds because the more the lists divides the easier it is for bubble sort to perform.
Implementation and Coding

Students will write code to implement the sorting algorithms in a programming language of Python




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
arr7 = [4,7,-1,-3,8,99,-99,11,1,0-]

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

start1 = time.time_ns()
bubble_merge(arr7)
end1 = time.time_ns()
print("The run time of the bubble_merge: " + str(end1-start1))



<img width="717" alt="Screenshot 2023-10-11 at 4 16 13 PM" src="https://github.com/DaboiCharles/CMPSC-463-Project-1-Charles-Langley/assets/79470963/eec2df2a-3092-4c30-b20f-86af3f17b79d">



Performance Analysis

When looking at the results it seems that Bubble Sort performed the best based on the tests that I gave it. What I found interesting was when looking at the results my bubble merge did better than the base merge sort. This makes sense because my bubble merge sorts as it's getting divided and it does divide all the way to the base case. I believe quick sort didn’t perform as well as it should have due to its pivot selection. Lastly, Insertion did the second best but again I believe it is due to the tests that I gave it. I didn’t make the arrays extremely long so I can imagine the longer the array the worst insertion sort will perform since it has to go one by one. My bubble merge isn’t the most efficient algorithm but it didn’t perform the worst which is a good step. A way my bubble merge could be improved is possibly by adding another division of the array. This way it’ll have an easier time using the bubble sort on a smaller array

