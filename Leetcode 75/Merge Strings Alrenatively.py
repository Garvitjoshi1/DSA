word1 = "abc"
word2 = "pqr"
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        arr = []
        n = len(word1)
        m = len(word2)

        if n > m:
            for i in range(0, m):
                arr.append(word1[i])
                arr.append(word2[i])
            arr.append(word1[m:n])

        elif m > n:
            for i in range(0, n):
                arr.append(word1[i])
                arr.append(word2[i])
            arr.append(word2[n:m])

        else:
            for i in range(0, n):
                arr.append(word1[i])
                arr.append(word2[i])
                
        return "".join(arr)