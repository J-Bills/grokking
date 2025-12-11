from bisect import bisect_left
""" Binary Seacrh 
    Time complexity: Takes O(logn) time
    Use case: When you have large amounts of sorted data.
    Better than Linear Search because we can discard half of the data set each time we do a step
    
    We can also use the bisect_left method from the bisect library to use a binary search without the extra code
"""

def binary_search(input_list, target):
    """ 
    A binary search searches for an element in a list by dividing it into halves. The first step in binary search is to locate the middle number.
    Then determing whether the number you are looking for is greater than or less than the middle number.
    If the number is less than the target number then we have no reason to search the lower half of the list.
    So we discard the lower half and repeat the process.
    """
    first = 0
    last = len(input_list) -1
    while (last >= first):
        mid = (first + last) // 2
        if target == input_list[mid]:
            return True
        else:
            if target < input_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False


def main():
    a_list = [n for n in range(10,20)]
    answer = binary_search(input_list=a_list, target=19)
    print(answer)
    answer = bisect_left(a_list, 19)
    print(answer)

if __name__ == "__main__":
    main()