class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a dictionary to count characters in magazine
        char_count = {}
        
        # Count characters in magazine
        for char in magazine:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Check if ransomNote can be constructed

        for char in ransomNote:
            if char_count.get(char, 0) <= 0:
                print('call')
                return False
            char_count[char] -= 1
        
        return True

# Example usage:
solution = Solution()
# print(solution.canConstruct("a", "b"))  # Output: False
# print(solution.canConstruct("aa", "ab"))  # Output: False
print(solution.canConstruct("aa", "aab"))  # Output: True
