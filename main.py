def linear_search(arr, target):
    length = len(arr)
    if length < 1:
        print("Array is empty")
        return -1
    for i in range(length):
        if arr[i] == target:
            print(i)
            return i
    print("Not found")
    return -1

def binary_search(arr, target):
    length = len(arr)
    left = 0
    right = length - 1
    if length < 1:
        print("Array is empty")
        return -1
    while left <= right:
        mid = left + (right - left // 2)
        if arr[mid] == target:
            print(mid)
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print("Not found")
    return -1

def is_palindrome(text):
    length = len(text)
    left = 0
    right = length - 1
    if length < 1:
        print("Text is empty")
        return False
    while left < right:
        if text[left] != text[right]:
            print('False')
            return False
        left += 1
        right -= 1
    print('True')
    return True

def rotate_array(arr, pos):
    length = len(arr)
    if pos < 1:
        print("Positions are not greater than 0")
        return
    if length < 1:
        print("Array is empty")
        return
    print(arr)
    k = pos % length
    reverse(arr, 0, length - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, length - 1)
    print(arr)

def reverse(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

def longest_substring_without_repeating_characters(text):
    length = len(text)
    left = 0
    mx = 0
    right = 0
    seen = []

    while right < length:
        if text[right] in seen:
            seen.pop(0)
            left += 1
        else:
            seen.append(text[right])
            right += 1
            mx = max(mx, right - left)
    print(mx)
    return mx

def longest_substring_without_repeating_characters_optimized(txt):
    length = len(txt)
    left = 0
    mx = 0
    seen = set()

    for right in range(length):
        while txt[right] in seen:
            seen.remove(txt[left])
            left += 1
        seen.add(txt[right])
        mx = max(mx, right - left + 1)
    print(mx)
    return mx

a = 'geeksforgeeks'
# Output: 7
b = 'aaa'
# Output: 1
c = 'abcdefabcbb'
# Output: 6
d = "abcabcbb"
# Output: 3
e = "bbbbb"
# Output: 1
f = "pwwkew"
# Output: 3
g = "abba"
# Output: 2

# Test cases
test_cases = {
    'a': ('geeksforgeeks', 7),
    'b': ('aaa', 1),
    'c': ('abcdefabcbb', 6),
    'd': ('abcabcbb', 3),
    'e': ('bbbbb', 1),
    'f': ('pwwkew', 3),
    'g': ('abba', 2),
    'h': ('abbaac', 2),
    'i': ('abcade', 5),
    'j': ('abcbdeac', 5),
    'k': ('abbaabcde', 5),
}

# Run tests
for key, (text, expected) in test_cases.items():
    actual = longest_substring_without_repeating_characters_optimized(text)
    result = "Correct ✅" if actual == expected else "Incorrect ❌"
    print(f"{key}: Expected {expected}, Actual {actual} — {result}")



