# Count the number of odd numbers in a given integer.

# Sample:
# f(0) -> 0
# f(123) -> 2
# f(-123) -> 2

## Solution
- Time complexity: O(n)
- Space complexity: O(1)

```python

# Method 1
def countOddNums(num):

    # Convert the integer to a string and remove the negative 
    # sign if present with the absolute value function.
    num = str(abs(num))

    oddCount = 0
    # for every character in the string
    for digit in num:
        # find the remainder of a division between two numbers
        if int(digit) % 2 == 1:
            oddCount +=1
    return oddCount

print(countOddNums(0))
print(countOddNums(123))
print(countOddNums(-123))

# Method 2
def countOddNums(num):

    # Handle negative numbers
    num = abs(num)
    oddCount = 0

    while num > 0:
        digit = num % 10 # Get the last digit
        if digit % 2 == 1: # Check if the digit is odd
            oddCount +=1
        num //= 10  # Remove the last digit using floor division, rounds the result down to the nearest whole number
    
    return oddCount

```
