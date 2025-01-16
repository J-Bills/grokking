In problems where we deal with sorted arrays (or linked-lists) and need to find a set of elements that fulfill certain constraints, the Two Pointers approach becomes quite useful. The set of elements could be a pair, a triplet or even a subarray. For example, take a look at the following problem:

**Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.**

To solve this problem, we can consider each element one by one (indicated by the first pointer) and iterate through the remaining elements (indicated by the second pointer) to find a pair with the given sum. The time complexity of this algorithm will be ,O(N^2) where 'N' is the number of elements in the input array.

Given that the input array is sorted, an efficient approach would be to start with one pointer at the beginning and another pointer at the end. At every step, we will check if the numbers indicated by the two pointers add up to the target sum. If they do not, we have two options:

1. If the sum of the two numbers indicated by the two pointers is greater than the target sum, this means that we need a pair with a smaller sum. To explore more pairs, we can decrement the end-pointer.
2. If the sum of the two numbers indicated by the two pointers is smaller than the target sum, this means that we need a pair with a larger sum. To explore more pairs, we can increment the start-pointer.

Here is the visual representation of this algorithm:

![Image](https://www.designgurus.io/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fdownload%2Fstorage%2Fv1%2Fb%2Fdesigngurus-prod.appspot.com%2Fo%2FdocImages%252F638c9e2788f1e1c16f41c35c%252Fimg%3A2b3f8b7-54f6-dbac-75e3-6b30e7e2ceec.png%3Fgeneration%3D1670160116717567%26alt%3Dmedia&w=3840&q=75&dpl=dpl_7tDZU8noR7auHUZHgvC7k4YyL3ah)

The time complexity of the above algorithm will be O(N).

### **Summary Table**

|**Pattern**|**Example**|**Time Complexity**|
|---|---|---|
|Single Pass|Two Sum in sorted array, Reverse array|O(n)O(n)|
|Nested Traversal|Three Sum, Subarray counting|O(n2)O(n2)|
|Sliding Window|Longest substring, Minimum subarray|O(n)O(n)|
|Combined with Binary Search|Pair with sum using sorting|O(nlog⁡n)O(nlogn)|