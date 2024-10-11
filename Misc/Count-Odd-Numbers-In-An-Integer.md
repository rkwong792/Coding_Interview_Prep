# Count the number of odd numbers in a given integer.

# Sample:
# f(0) -> 0
# f(123) -> 2
# f(-123) -> 2

## Solution
- Time complexity: O(n)
- Space complexity: O(1)

```python
def countOddNums(num):

    # Convert the integer to a string and remove the negative 
    # sign if present with the absolute value function.
    num = str(abs(num))

    oddCount = 0
    # for every character in the string
    for digit in num:
        if int(digit) % 2 == 1:
            oddCount +=1
    return oddCount

print(countOddNums(0))
print(countOddNums(123))
print(countOddNums(-123))

```
