# Encode and Decode Strings

> - Difficulty: Medium
> - Type: Array & Hashing
> - [link](https://leetcode.com/problems/encode-and-decode-strings/)

## Solution
- Time complexity: O(N)
- Space complexity: O(N)
- *Hint: In the decode() function, the `j` variable is tasked to point to the delimiter.*

```python
class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s   # Store length + '#' + actual string
        return res

    def decode(self, s: str) -> list[str]:
        """Decodes a single string back to a list of strings."""
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res
```

## Run Locally:

```python
class Codec:
    def encode(self, strs):
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word)) + "#" + word
        return encoded_str
    
    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            j = i
            # find where # is
            while s[j] != '#':
                j+=1
            
            # at this point, j is on #
            length = int(s[i:j])
            res.append(s[j+1: j+1+length])

            i = (j+1+length)
        
        return res

codec = Codec()

# Test case 1
strs = ["hello", "world"]
encoded = codec.encode(strs)
print("Encoded:", encoded)  # Expected: "5#hello5#world"
decoded = codec.decode(encoded)
print("Decoded:", decoded)  # Expected: ["hello", "world"]

# Test case 2
strs = ["abcd", "efgh", "ijkl"]
encoded = codec.encode(strs)
print("Encoded:", encoded)  # Expected: "4#abcd4#efgh4#ijkl"
decoded = codec.decode(encoded)
print("Decoded:", decoded)  # Expected: ["abcd", "efgh", "ijkl"]

# Test case 3 (empty list)
strs = []
encoded = codec.encode(strs)
print("Encoded:", encoded)  # Expected: ""
decoded = codec.decode(encoded)
print("Decoded:", decoded)  # Expected: []

# Test case 4 (list with empty strings)
strs = ["", "hello", "", "world"]
encoded = codec.encode(strs)
print("Encoded:", encoded)  # Expected: "0#0#hello0#0#world"
decoded = codec.decode(encoded)
print("Decoded:", decoded)  # Expected: ["", "hello", "", "world"]
```