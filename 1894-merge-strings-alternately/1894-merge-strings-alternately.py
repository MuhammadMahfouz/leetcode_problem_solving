class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        merg_str = []

        len1, len2 = len(word1), len(word2)
        max_len = max(len1, len2)

        for i in range(max_len):
            if i < len1:
                merg_str.append(word1[i])
            if i < len2:
                merg_str.append(word2[i])
            
        return "".join(merg_str)
                