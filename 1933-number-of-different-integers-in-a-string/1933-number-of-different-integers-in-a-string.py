class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        i = 0
        int_set = set()
        while i < len(word):
            if word[i].islower():
                i += 1
                continue
            j = i + 1
            while j < len(word) and word[j].isdigit():
                j += 1
            int_set.add(int(word[i:j]))
            i = j + 1
        return len(int_set)