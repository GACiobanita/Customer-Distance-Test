# Customer-Distance-Test

Installation instructions - Windows 10:
1. Download Python version 3.7.4. from https://www.python.org/downloads/, makes sure you have the following modules installed: math, unittest, random and timeit
2. Download Customer-Distance-Test-1.0.tar.gz and extract the contents where you see fit.
3. In the Command Prompt, inside the project folder, run the following line: python -m implementation.main
	Example: C:\Users\Alex\Python\Customer-Distance-Test-1.0>python -m implementation.main
4. Enter a file path in the format: C:\Users\Alex\Python\Customer-Distance-Test-1.0\customers.txt, or simply press enter to use the default file.

Algorithms implemented:
Implementations for Merge sort, Quick sort and Binary Search Tree have been used.
Algorithm selection was based on the fact that they are well known and simple, while the Python library makes use of Timsort(a combination of Merge sort and Insertion sort).
A. Merge sort: 
Branch merge_sort-usage shows the implementation of the merge sort algorithm when displaying the customers in a sorted order.

Run || Time
 1. || 0.015755793999999934
 2. || 0.0161657540000002
 3. || 0.01544903700000022
 4. || 0.013572573000000032
 5. || 0.016923522999999996
Average: 0.0155733362000000764

B. Quick sort:
Branch quick_sort-usage shows the implementation of the merge sort algorithm when displaying the customers in a sorted order.

Run || Time 
 1. || 0.008922753000000005
 2. || 0.008122218999999653
 3. || 0.012005717999999943
 4. || 0.012026244999999935
 5. || 0.009959910000000072
Average: 0.0102073689999999216

C. Binary Search Tree:
Branch binary_search_tree-usage shows the implementation of the binary search tree including node implementation. This implementation has the advantage
that nodes are placed in the tree in a sorted order on the fly, with left and right side rule of small and large. This allows the implementation of 
functions that simply traverse the tree. For this reason the binary_search_tree-usage branch has been merged into the main branch and further changes
appear from that point.

Run || Time
 1. || 0.008265905000000018
 2. || 0.00835428199999999
 3. || 0.009656004999999857
 4. || 0.008036691999999901
 5. || 0.008420423999999871
Average: 0.0085466615999999274

Future Targets:
1. The implementation of a command line interface, similar to Python when passing extra commands.
2. Feature of changing the target location(changing the location from Dublin to another location).
3. Measurement of memory usage, as all algorithms at the moment store the entire file in memory, a line by line approach could save memory and/or speed up the creation of the client list.
4. A better implementation of the check_json_data(data) function from user_inviter.py, I do not like how I've ended up implementing this function as files(and keys) could change in the future.
5. On the fly sorting for Merge sort and Quick sort can show better performance.

