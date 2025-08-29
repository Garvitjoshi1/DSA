class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr = []
        m = max(candies)
        for i in candies:
            arr.append(i+extraCandies >= m)
        return arr