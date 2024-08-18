"""
Determine if a string is unique. A unique string has no repeating characters.
Do not use any additional storage/ data structures.
"""

def isUnique(string):
    check = 0
    for char in string:
        index = ord(char) - ord("a")
        
        # Check if the bit at position index is already set
        if check & (1 << index):
            return False
        
        # Set the bit at position index
        check |= (1 << index)
    return True

print(f"Return True: {isUnique("abc")}")
print(f"Return False: {isUnique("aba")}")