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
	Check the python files for the coding and Implentation


<img width="717" alt="Screenshot 2023-10-11 at 4 16 13 PM" src="https://github.com/DaboiCharles/CMPSC-463-Project-1-Charles-Langley/assets/79470963/eec2df2a-3092-4c30-b20f-86af3f17b79d">



Performance Analysis

When looking at the results it seems that Bubble Sort performed the best based on the tests that I gave it. What I found interesting was when looking at the results my bubble merge did better than the base merge sort. This makes sense because my bubble merge sorts as it's getting divided and it does divide all the way to the base case. I believe quick sort didn’t perform as well as it should have due to its pivot selection. Lastly, Insertion did the second best but again I believe it is due to the tests that I gave it. I didn’t make the arrays extremely long so I can imagine the longer the array the worst insertion sort will perform since it has to go one by one. My bubble merge isn’t the most efficient algorithm but it didn’t perform the worst which is a good step. A way my bubble merge could be improved is possibly by adding another division of the array. This way it’ll have an easier time using the bubble sort on a smaller array

