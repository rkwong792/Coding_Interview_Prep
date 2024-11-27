# Integer to Roman

> - Difficulty: Medium
> - [link](https://leetcode.com/problems/integer-to-roman/)

## Solution
- Time complexity: O(1)
- Space complexity: O(1)

```python
class Solution:
    def intToRoman(num):
    # Step 1: List the values and their symbols
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    # Step 2: Start with an empty string
    roman = ""
    
    # Step 3: Loop through the values
    for i in range(len(val)):
        while num >= val[i]:  # Can we subtract this value?
            roman += symbols[i]  # Write the symbol
            num -= val[i]        # Subtract the value
    
    # Step 4: Return the result
    return roman

```