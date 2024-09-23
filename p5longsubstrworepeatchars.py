def length_of_longest_substring(s):
    # Set to store the characters in the current window
    char_set = set()
    
    # Pointers and result variable
    start = 0
    max_length = 0

    # Iterate through the string with `end` as the pointer
    for end in range(len(s)):
        # If the character is already in the set, shrink the window from the left
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        
        # Add the current character to the set
        char_set.add(s[end])

        # Update the max length of the substring
        max_length = max(max_length, end - start + 1)
    
    return max_length


s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: 3