"""
5. Longest Palindromic Substring
Solved
Medium
Topics
Companies
Hint
Given a string s, return the longest 
palindromic
 
substring
 in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


def get_longest_palindromic_substring(string: str) -> int:
    memory = {}  # Key (curr, prev): maximum length
    return recursive(string, 1, 0, memory)


def recursive(
    string: str, curr: int, prev: int, memory: dict[tuple[int, int], int]
) -> int:
    """
    ababasdfkkadsjjxkahlskjhajkchvaabbbbbaaaajkchasjkdhfaxxxxxxxxxxxxxxxxxxxx
    1. Stop Condition
    2. Programming Logic
      - 當前是不是 palindromic substring,
      - 保留
      - 不保留
    """
    if curr == len(string):
        return curr - prev if is_palindromic(string[prev:curr]) else 0
    # 當前 palidromic
    # 不保留 palindromic
    # 保留 palindormic

    # duplicate visit ?
    if (curr, prev) in memory:
        return memory[(curr, prev)]

    # if not visited before
    curr_result = 0
    if is_palindromic(string[prev:curr]):
        curr_result = curr - prev

    reserved_result = recursive(string, curr + 1, prev, memory)
    non_reserved_result = recursive(string, curr + 1, curr, memory)

    result = max(curr_result, reserved_result, non_reserved_result)
    memory[(curr, prev)] = result  # Save the result
    return result


def is_palindromic(string: str) -> bool:
    """Your work, NOTE: edge case"""
    ptr1, ptr2 = 0, len(string) - 1
    while ptr1 < ptr2:
        if string[ptr1] != string[ptr2]:
            return False
        ptr1 += 1
        ptr2 -= 1
    return True


def main():
    test1 = "a"
    test2 = "aba"
    test3 = "abcdeeeee"
    test4 = "abbacddcettttttttttttttttttttttttttttttttttttttteabcdefg"
    print(get_longest_palindromic_substring(test1))
    print(get_longest_palindromic_substring(test2))
    print(get_longest_palindromic_substring(test3))
    print(get_longest_palindromic_substring(test4))


main()


"""
test4 = "abbacddcettttttttttttttttttttttttttttttttttttttteabcdefg"
        a
    ab     b
abb   b  bb   b
"""
