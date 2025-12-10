import functools
import logging

logging.basicConfig(
    level = logging.INFO,
    format= '[%(levelname)s] %(funcName)s: '
)


def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"--- Running function: {func.__name__} ---")
        result = func(*args, **kwargs)
        return result
    return wrapper
"""
HCL Python Automation Engineer — DSA Practice Pack
Author: You

Instructions:
- Each function has a short docstring and TODO marker.
- Implement directly in this file, then run `pytest` or simple prints.
- Focus on clarity and basic Python logic — these are the kinds of
  warm-up problems often used to gauge comfort with loops, lists,
  strings, and recursion.
"""

# -------------------- STRINGS --------------------
@log_function_call
def reverse_string(s: str) -> str:
    """Return the reverse of s. Example: 'abc' -> 'cba'."""
    logging.info('starting this function.')
    # TODO: implement
    r_string  = s[::-1]
    return r_string
    

@log_function_call
def is_palindrome(s: str) -> bool:
    """Return True if s reads the same forward and backward."""
    # TODO: implement
    s = s.lower()
    return s == s[::-1]
    

@log_function_call
def char_frequency(s: str) -> dict[str, int]:
    """Return dict of character frequencies in s."""
    # TODO: implement
    freqs: dict[str, int] = {}
    for ch in s:
        freqs[ch] = freqs.get(ch,0) + 1
    return freqs
    

@log_function_call
def first_unique_char(s: str) -> str | None:
    """Return first non-repeating character or None if none."""
    # TODO: implement
    freqs: dict[str, int] = {}
    for ch in s:
        freqs[ch] = freqs.get(ch, 0) + 1
    for ch in s:
        if freqs[ch] == 1:
            return ch
    return None

@log_function_call
def reverse_words(sentence: str) -> str:
    """Reverse order of words in a sentence."""
    # TODO: implement
    reverse_sentence = " ".join(sentence.split()[::-1])
    return reverse_sentence


# -------------------- LISTS --------------------
@log_function_call
def find_min_max(nums: list[int]) -> tuple[int, int]:
    """Return (max, min) of nums."""
    # TODO: implement
    return max(nums), min(nums)
    

@log_function_call
def unique(nums: list[int]) -> list[int]:
    """Return list with duplicates removed (preserve order)."""
    # TODO: implement
    seen: set[int] = set()
    result: list[int] = list()
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

@log_function_call
def second_largest(nums: list[int]) -> int:
    """Return the 2nd largest number in nums."""
    # TODO: implement
    first = max(nums)
    nums = [n for n in nums if n != first]
    return max(nums)
@log_function_call
def second_largest_two(nums:list[int]) -> str:
    """Return the 2nd largest number in nums and it's position in the array."""
    """ O(n) version """
    # TODO: implement
    first=second=float('-inf')
    first_idx = second_idx = -1
    for i, n in enumerate(nums):
        if n > first:
            second, second_idx = first, first_idx
            first = n
        elif first > n and n > second:
            second, second_idx = n, i
    if second == float('-inf'):
        raise ValueError('Need at least 2 distinct numbers')
    return f"second (value, pos): {(second, nums.index(second))}"

@log_function_call
def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    """Merge two sorted lists into one sorted list."""
    # TODO: implement
    i=j=0
    merged_list: list[int] = list()
    while i< len(a) and j< len(b):
        if a[i] <= b[j]:
            merged_list.append(a[i])
            i+=1
        else:
            merged_list.append(b[j])
            j+=1
    if i< len(a):
        merged_list.extend(a[i:])
    elif j< len(b):
        merged_list.extend(b[j:])
    return f'merged list is {merged_list}'

@log_function_call
def missing_number(nums: list[int]) -> int:
    """Given list 1..n missing one, return missing number."""
    # TODO: implement
    if not all(isinstance(x, int) for x in nums):
        raise ValueError('nums must contain only integers')
    n = len(nums)+1
    
    return n * (n + 1) // 2 - sum(nums)

@log_function_call
def missing_number2(nums: list[int]) -> int:
    if not all(isinstance(x, int) for x in nums):
        raise ValueError('nums must contain only integers')
    n = len(nums)+1
    nums_set = set(nums)
    compare_set = set(range(1, n+1))
    result = compare_set.difference(nums_set).pop()
        
    return 'compare set:',compare_set

# -------------------- RECURSION --------------------
@log_function_call
def factorial(n: int) -> int:
    """Return factorial of n (n!)."""
    # TODO: implement
    if n<=1: return 1
    return n*factorial(n-1)


@log_function_call
def fibonacci(n: int) -> int:
    """Return nth Fibonacci number (0-indexed)."""
    # TODO: implement
    if n<0:
        raise ValueError('n must be non-negative')
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@log_function_call
def tower_of_hanoi(n: int, src: str, dst: str, aux: str) -> list[tuple[str, str]]:
    """Return list of (from,to) moves to solve Tower of Hanoi."""
    # TODO: implement
    pass


# -------------------- SEARCHING --------------------
@log_function_call
def binary_search(arr: list[int], target: int) -> int:
    """Return index of target in sorted arr, or -1 if not found."""
    # TODO: implement
    pass

@log_function_call
def count_words_in_file(file_path: str) -> int:
    """Return number of words in a text file."""
    # TODO: implement
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    words = text.split()
    return len(words)


# -------------------- BONUS --------------------
@log_function_call
def are_anagrams(a: str, b: str) -> bool:
    """Return True if a and b are anagrams (ignore case/spaces)."""
    # TODO: implement
    a = a.strip().lower()
    b = b.strip().lower()
    
    if len(a) != len(b):
        return False
    hash_map_a: dict[str, int] = dict()
    for char in a:
        hash_map_a[char] = hash_map_a.get(char, 0) +1
    for char in b:
        if char not in hash_map_a:
            return False
        hash_map_a[char] -= 1
        if hash_map_a[char] < 0:
            return False
    return True

@log_function_call
def flatten_nested_list(lst: list) -> list:
    """Flatten nested lists into one list. Example: [1,[2,3],[4]] -> [1,2,3,4]."""
    # TODO: implement
    pass

@log_function_call
def sum_of_digits(n: int) -> int:
    """Return sum of digits using loop or recursion."""
    # TODO: implement
    if n<10:
        return n
    return (n%10 + sum_of_digits(int(n/10)))


# -------------------- SIMPLE SELF TESTS --------------------
if __name__ == "__main__":
    print(reverse_string("abc"))        # cba
    print(is_palindrome("level"))       # True
    print(char_frequency('hello'))
    print(first_unique_char('aabbcddee'))
    print(reverse_words('hello world'))
    print(unique([1,2,2,3,1]))          # [1,2,3]
    print(second_largest([1,2,2,10,2,3,10]))
    print(second_largest_two([1,2,2,10,2,3,10]))
    print(merge_sorted([1,3,5,7,9], [2,4,6]))
    print(missing_number([1,2,4,5]))
    print(missing_number2([1,2,4,5]))
    print(find_min_max([5,2,9,1,5]))    # (9,1)
    print(factorial(5))        # 120
    print(fibonacci(10))
    print(binary_search([1,3,5,7,9],7)) # 3
    print(sum_of_digits(12345))
    print(are_anagrams('fried', 'fired'))
