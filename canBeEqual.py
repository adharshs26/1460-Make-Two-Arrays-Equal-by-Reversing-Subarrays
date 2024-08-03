class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:

        if len(target) != len(arr):
            return False
        
        # Compare element frequencies in both arrays
        return Counter(target) == Counter(arr)
