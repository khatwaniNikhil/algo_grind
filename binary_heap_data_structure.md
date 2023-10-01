# Data structure versus garbage collected heap
1. heap ds is a tree like data structure wherea gc heap is just a pile/collection of memory/ram

# visualise
1. **nearly complete** **ordered** binary tree
2. all levels are filled except the lowest and the lowest level is filled  up to a certain point starting from the left

# Type
1. min-heap (parent is less than left and right child)
2. max-heap (parent is greater than left and right child)

  ![](https://i.ytimg.com/vi/86mQ1gD3Zgg/maxresdefault.jpg)

# Use cases
1. max heaps are used for heap sort
2. min heaps are great for priority queues

# Store Heap as array
1. for a given node at index i in array, refer the formula to look up index of left, right and parent node.
  ![](https://github.com/khatwaniNikhil/algorithms/blob/main/images/heap_store_in_array.png)
  
# Operations
1. build-max-heap (from unsorted array)
![](https://github.com/khatwaniNikhil/algorithms/blob/main/images/build_max_heap.png)

2. heapify (similar to build-max-heap but faster as it assumes array is already sorted)

# HEAP-SORT
## challenge
1. Given an array to sort

## solution
Repeat following steps
1.  build max heap to find the largest item
2.  remove that item from the heap and place removed item into a sorted partition
    1. by swapping with the item at the end of the array)

# Time complexity
1. BUILD‐MAX‐HEAP(unordered input array) - O(n)
2. MAX‐HEAPIFY - O(logn)
3. HEAPSORT  - O(nlogn)


finally we remove nine from the tree and consider  it sorted looks good so far except we're back to  
having a tree and not a heap this time we call  heapify since only the item one is out of place
one floats down to the bottom and  the largest number heads to the top
we're back to having a max-heap let's swap  the largest number 8 with the item at the  
end of the unsorted part of the array  2 we remove 8 and consider it sorted
again we need our heat back so let's call heapify
