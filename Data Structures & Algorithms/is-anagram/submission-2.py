class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1=Counter(s)
        hash2=Counter(t)
        return hash1==hash2
        