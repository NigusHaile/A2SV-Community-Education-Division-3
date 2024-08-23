class Solution:
    def similarPairs(self, words: List[str]) -> int:

        sets = []
        for word in words:
            char_set = set(word)
            sets.append(char_set)

        count = 0
        n = len(words)
        
        for i in range(n):
            for j in range(i + 1, n):
                if sets[i] == sets[j]:
                    count += 1
        
        return count
