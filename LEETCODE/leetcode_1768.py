class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        max_len = max(len(word1), len(word2))

        for i in range(max_len):
            if i < len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])

        return ''.join(merged)


if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeAlternately("abc", "pqr"))  # 期待値: apbqcr
    print(sol.mergeAlternately("ab", "pqrs"))  # 期待値: apbqrs
    print(sol.mergeAlternately("abcd", "pq"))  # 期待値: apbqcd
    print(sol.mergeAlternately("", "xyz"))     # 期待値: xyz
    print(sol.mergeAlternately("hello", ""))   # 期待値: hello
