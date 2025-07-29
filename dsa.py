class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        char_map = {}
        n = len(s)

        max_len = 0
        start = 0

        for i in range(n):
            if s[i] in char_map.keys():
                start = char_map[s[i]] + 1

            max_len = max(max_len, i - start + 1)
            char_map[s[i]] = i

        return max_len


s = Solution()
print(s.lengthOfLongestSubstring("abba"))