"""
Longest Palindromic Substring 

abbaegggge


Longest Palindromic Subsequence
aefehwggwee

eewwee
eewggwee

abcde
   |
a
b
c
ac
bcd


a
"""


def get_longest_subsequence(string) -> int:
    memory = {}
    return recursive(string, 0, "", memory)


def recursive(string, ptr, accumulated_string: str, memory: dict[str, int]):
    """
    1. Boundary Condition 什麼時候停止
    2. 過程中做什麼事情
    3. 要回傳什麼

    "abcdaaa"
    "a"

        ""
        /  \
      "a"   ""
      / \
    "ab"  "a"
    """
    if ptr >= len(string):
        if is_palindrome(accumulated_string):
            return len(accumulated_string)
        return 0
    if accumulated_string in memory:
        return memory[accumulated_string]

    curr_char = string[ptr]
    curr_value = 0

    if is_palindrome(accumulated_string):
        curr_value = len(accumulated_string)

    reserved_result = recursive(string, ptr + 1, accumulated_string + curr_char, memory)
    non_reserved_result = recursive(string, ptr + 1, accumulated_string, memory)

    result = max(curr_value, reserved_result, non_reserved_result)
    memory[accumulated_string] = result
    return result


def is_palindrome(string: str) -> bool:
    ptr1, ptr2 = 0, len(string) - 1
    while ptr1 < ptr2:
        if string[ptr1] != string[ptr2]:
            return False
        ptr1 += 1
        ptr2 -= 1
    return True


def main():
    # print(get_longest_subsequence("aba"))
    # time start

    print(get_longest_subsequence("abcdaaafaaserwqgasdafg"))
    # print(get_longest_subsequence("abadbdaba"))
    # print(get_longest_subsequence("abcdefg"))
    # print(get_longest_subsequence(""))


main()
