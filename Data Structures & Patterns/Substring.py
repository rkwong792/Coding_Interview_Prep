# In Python string slicing, the end index is always exclusive. 
# This means that when you slice a string using s[start:end], the substring will include characters starting from start 
# but will not include the character at the end index.

# 1. Basic Slicing
s = "abcdef"

# Extracting from index 1 to 4 (exclusive of index 4)
substring = s[1:4]
print(substring)  # Output: "bcd"


# 2. Basic String Interpolation
s = "abcdef"

# Extract every second character starting from index 0
substring = s[0:6:2]
print(substring)  # Output: "ace"

# Extract every second character starting from index 1
substring = s[1:6:2]
print(substring)  # Output: "bd"


# 3. Negative Indices (From the end)
s = "abcdef"

# Extracting from the 2nd to the last character (using negative index)
substring = s[-4:-1]
print(substring)  # Output: "cde"

# Extracting the last 3 characters
substring = s[-3:]
print(substring)  # Output: "def"

