class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd=sorted(s)
        td=sorted(t)
        return sd==td