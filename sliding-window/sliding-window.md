In many problems dealing with an array (or a LinkedList), we are asked to find or calculate something among all the subarrays (or sublists) of a given size. For example, take a look at this problem:

Given an array, find the average of each subarray of ‘K’ contiguous elements in it.

Let's understand this problem with an example:

Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Here, we are asked to find the average of all subarrays of '5' contiguous elements in the given array. Let's solve this:

For the first 5 numbers (subarray from index 0-4), the average is: 
The average of next 5 numbers (subarray from index 1-5) is: 
For the next 5 numbers (subarray from index 2-6), the average is: 
...
Here is the final output containing the averages of all subarrays of size 5:

Output: [2.2, 2.8, 2.4, 3.6, 2.8]
A brute-force algorithm will calculate the sum of every 5-element subarray of the given array and divide the sum by '5' to find the average. This is what the algorithm will look like:

```python
class Solution:
  def findAverages(self, K, arr):
    result = []
    for i in range(len(arr)-K+1):
      # find sum of next 'K' elements
      _sum = 0.0
      for j in range(i, i+K):
        _sum += arr[j]
      result.append(_sum/K)  # calculate average

    return result


def main():
  sol = Solution()
  result = sol.findAverages(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()
```

Time Complexity
Outer loop: The outer loop runs for each possible starting index of a subarray of size K. Since the array has N elements, the outer loop runs N-K+1 times, which is approximately O(N) .

Inner loop: For each iteration of the outer loop, the inner loop runs for K elements to calculate the sum of the subarray. Since the inner loop runs  times for each iteration of the outer loop, the total time complexity is O(N*K).

Overall time complexity: O(N*K).

Can we find a better solution? Do you see any inefficiency in the above approach?

The inefficiency is that for any two consecutive subarrays of size '5', the overlapping part (which will contain four elements) will be evaluated twice. For example, take the above-mentioned input:

Image
As you can see, there are four overlapping elements between the subarray (indexed from 0-4) and the subarray (indexed from 1-5). Can we somehow reuse the sum we have calculated for the overlapping elements?

The efficient way to solve this problem would be to visualize each subarray as a sliding window of '5' elements. This means that we will slide the window by one element when we move on to the next subarray. To reuse the sum from the previous subarray, we will subtract the element going out of the window and add the element now being included in the sliding window. This will save us from going through the whole subarray to find the sum and, as a result, the algorithm complexity will reduce to .

```python
class Solution:
  def findAverages(self, K, arr):
      result = []
      windowSum, windowStart = 0.0, 0
      for windowEnd in range(len(arr)):
          windowSum += arr[windowEnd]  # add the next element
          # slide the window, no need to slide if we've not hit the required window size of 'k'
          if windowEnd >= K - 1:
              result.append(windowSum / K)  # calculate the average
              windowSum -= arr[windowStart]  # subtract the element going out
              windowStart += 1  # slide the window ahead

      return result


def main():
  sol = Solution()
  result = sol.findAverages(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()
```

Time Complexity

Single pass: The algorithm only requires one pass through the array to calculate the sum of subarrays of size K. The loop runs for each element of the array, so the time complexity is O(N) , where N is the number of elements in the array.

Sliding window: The sliding window approach ensures that we add a new element to the sum and subtract the outgoing element in constant time, . As a result, for each subarray of size K, we perform constant-time operations. This avoids the need to re-calculate the sum for overlapping subarrays repeatedly, making it much more efficient than the nested loop approach.

Overall time complexity: O(N).
