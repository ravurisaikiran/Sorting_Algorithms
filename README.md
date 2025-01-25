Argue of selection sort correctness:-

1. Selection sort is correct because it pin points the well-defined sorting algorithm process which is ensuring all the elements in the array are stored in an order after the algorithm completes it's task.

2. Here we use a loop varient, which is a property that is true before and after every iteration of a loop. 
At the start of the i-th iteration, the first i elements of the array are sorted and contain the smallest i elements in the correct order.


3. There are three points to proove the correctness,

> Initialization, where i=0 and the sorted section is empty (no elements are sorted yet). The invariant holds trivially.

> Maintenance, During the i-th iteration, the algorithm finds the smallest element in the unsorted section and swaps it with the element at the index i ensuring the element is placed accordingly. After the swap, the first i+1 elements are sorted, maintaining the loop invariant.
 
> Termination, where i=n-1, at this point the entire array is sorted, and the loop invariant ensures correctness

4.Time Complexity O(n2): While Selection Sort is correct, its performance is less efficient compared to other sorting algorithms.

# Sorting_Algorithms
Insertion_bubble_Selection-Algorithms

PS C:\Users\saiki> & C:/Users/saiki/AppData/Local/Programs/Python/Python313/python.exe d:/DAA-UTA/sorting_algorithms.py/sorting.py


SYSTEM INFO:

System: Windows 10.0.22631

Node Name: RAVURI

Release: 11

Machine: AMD64

Processor: Intel64 Family 6 Model 142 Stepping 12, GenuineIntel

CPU Frequency: 1609.00 MHz

CPU Cores: 4 physical, 8 logical

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Benchmarking Sorting Algorithms:

Input size: 5

Insertion Sort: 0.000028 seconds

Selection Sort: 0.000027 seconds 

Bubble Sort: 0.000037 seconds

------------------------------

Input size: 10 

Insertion Sort: 0.000029 seconds

Selection Sort: 0.000029 seconds

Bubble Sort: 0.000028 seconds

-----------------------------

Input size: 50

Insertion Sort: 0.000144 seconds

Selection Sort: 0.000257 seconds

Bubble Sort: 0.000289 seconds

-----------------------------

Input size: 100

Insertion Sort: 0.000592 seconds

Selection Sort: 0.000618 seconds

Bubble Sort: 0.002319 seconds

-----------------------------

Input size: 500

Insertion Sort: 0.018064 seconds

Selection Sort: 0.021816 seconds

Bubble Sort: 0.048822 seconds

-----------------------------

Input size: 1000

Insertion Sort: 0.097083 seconds

Selection Sort: 0.100771 seconds

Bubble Sort: 0.155705 seconds

-----------------------------

Input size: 2000

Insertion Sort: 0.144352 seconds

Selection Sort: 0.175557 seconds

Bubble Sort: 0.371443 seconds

-----------------------------

Input size: 5000

Insertion Sort: 0.666837 seconds

Selection Sort: 0.777922 seconds

Bubble Sort: 2.246128 seconds

![sorting figure](https://github.com/user-attachments/assets/e0fb74ad-7a60-47e7-8e7f-8c1fe8a425bb)
