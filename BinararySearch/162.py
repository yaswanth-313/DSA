class Solution:
    def findPeakElement(self, num: list[int]) -> int:
        left=0
        right=len(num)-1

        while left<right:
            mid=(left+right)//2

            if num[mid] < num[mid+1]:
                left=mid+1
            else:
                right=mid

        return right

        