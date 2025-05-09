# Anagram Checker: Check if two strings are anagrams (same letters, different order).


def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if sorted characters match
    return sorted(str1) == sorted(str2)

# Example usage
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

if is_anagram(s1, s2):
    print(f'"{s1}" and "{s2}" are anagrams.')
else:
    print(f'"{s1}" and "{s2}" are not anagrams.')

