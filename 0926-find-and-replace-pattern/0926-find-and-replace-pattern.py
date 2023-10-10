class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for i in words:
            mp = {}
            bp = {}
            isPattern = True
            for j in range(len(i)):
                if i[j] not in bp:
                    bp[i[j]] = pattern[j]
                else:
                    if bp[i[j]] != pattern[j]:
                        isPattern = False
                        break
                if pattern[j] not in mp:
                    mp[pattern[j]] = i[j]
                else:
                    if mp[pattern[j]] != i[j]:
                        isPattern = False
                        break
            if isPattern:
                ans.append(i)
        return ans
        