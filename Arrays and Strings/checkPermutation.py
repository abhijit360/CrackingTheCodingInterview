''' 
1.2 Check Permutation
Given two strings, write a method to decide if one is permutation of other.
'''

def checkPermutation(str_1 : str, str_2 :str):
    if len(str_1) != len(str_2):
        return False
    
    str_1 = ''.join(sorted(str_1))
    str_2 = ''.join(sorted(str_2))
    
    for index in range(len(str_1)):
        if str_1[index] != str_2[index]:
            return False
        
    return True

print("testing", checkPermutation("test","sett"))
        
    
