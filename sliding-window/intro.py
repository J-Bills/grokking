def brute_force():
    """Given an array, find the average of each subarray of K contiguous elements in it"""

    
    k = 5
    result = list()
    for i in range(len(array)-k+1):
        _sum = 0.0
        for j in range(i, i+k):
            _sum += array[j]
        result.append(_sum/k)
    print(result)
    
def optimal():
    """ Visualize each subarray as a sliding window of 5 elements"""
    """ slide the winow by one element when we move on
        and reuse the sum from the previous subarray by
        subtracting the element going out and adding the element coming in."""
    k = 5
    result = list()
    _sum, _start = 0.0, 0
    for _end in range(len(array)):
        _sum += array[_end]
        print(_sum)
        if _end >= k-1:
            result.append(_sum/k)
            _sum -=array[_start]
            _start +=1
    # print(result)
    
    # window_sum = sum(array[:k])
    # result = [window_sum]
    
    # for i in range(k, len(array)):
    #     window_sum += array[i]
    #     window_sum -= array[i-k]
    #     result.append(window_sum)
    
    # result = [x/k for x in result]
    # print(result)
if __name__ == "__main__":
    global array
    array = list([1,3,2,6,-1,4,1,8,2])
    optimal()
    
    