class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""       
        # first string as the prefix
        prefix = strs[0]       
        for text in strs[1:]:
            while text[:len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]       
            if not prefix:
                break    
        return prefix
