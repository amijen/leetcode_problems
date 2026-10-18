class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = []
        longest = 0
        for n in s:
            if n in L:
                L = L[L.index(n) + 1 :]
            L.append(n)
            longest = max(longest, len(L))
        return longest