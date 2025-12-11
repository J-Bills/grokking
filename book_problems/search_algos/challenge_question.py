""" Given a list of words in alphabetical order, write a function that performs a binary search for a word and returns whether it is in the list."""
def word_search(word_list, target):
    first_index = 0
    last_index = len(word_list) -1
    while first_index <= last_index:
        mid = (first_index + last_index) // 2
        if word_list[mid] == target:
            return True
        else:
            if word_list[mid] < target:
                first_index = mid + 1
            else:
                last_index = mid - 1
    return False
def main():
    sorted_fruits = ['apple', 'banana','kiwi', 'orange', 'plum']
    print(word_search(sorted_fruits, target='plum'))

if __name__ == "__main__":
    main()