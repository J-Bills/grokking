""" Linear Search
    Time complexity: O(n)
    When to use: Use it when the data in your list is not sorted
    Using the (in) keyword in python we can perform a linear search on a data structure.
    If our data is sorted then there are other search algo's that can be used in it's place."""

def linear_search(input_list, target):
    """ 
    In linear search you iterate through every element in a data set and compare it to the target number.
    If your comparison finds a match, the number is in the list.
    If the algo ends without finding a match, the number is not in the list.
    """
    for n in input_list:
        if n == target:
            return True
    return False

def main():
    a_list: list = list((1,8,32,91,5,15,9,100,3))
    answer = linear_search(input_list=a_list, target=17)
    print(answer)
if __name__ == "__main__":
    main()