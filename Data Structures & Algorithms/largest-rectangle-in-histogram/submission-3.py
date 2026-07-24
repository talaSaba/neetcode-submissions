# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         ##Brute Force ##
#         area=0
#         for i in range(len(heights)):
#             mm=float('inf')
#             for j in range(i+1,len(heights)):
#                 mm=min(mm,heights[j])
#                 current=mm*(j-i)
#                 area=max(area,current)
#         if area==0:
#             return heights[0]
#         return area
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0

        for i in range(len(heights)):
            mm = float("inf")

            for j in range(i, len(heights)):
                mm = min(mm, heights[j])
                current = mm * (j - i + 1)
                area = max(area, current)

        return area
                
