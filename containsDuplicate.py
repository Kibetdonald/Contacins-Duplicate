# Methods:
# 1. Sorting the array: Time complexity of O(n log n)
# 2. Brute force method: Time complexity of O(n²)
# 3. Harshset: Space compexity of O(n): (Most Preffered)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    # create hashset
    hashset = set()
    
    # for loop
    for i in nums:
        # Checks whether i exists in the harshset
        if i in hashset:
            return True
        hashset.add(i)
    return False
