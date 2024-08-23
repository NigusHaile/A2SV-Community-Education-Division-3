class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_characters = Counter(words[0])
        
        for word in words[1:]:
            character_count = Counter(word)
            common_characters &= character_count  

        result = []
        for char in common_characters:
            count = common_characters[char]
            result += [char] * count
        
        return result
