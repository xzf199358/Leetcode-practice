#coding= UTF-8

import  time
'''
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
画 n 条垂直线，使得垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
注意：你不能倾斜容器，n 至少是2。

该题目的解法为约束问题 因此 需要根据 约束条件 进行设置约束
这里的最大面积取决于  最低的高度值  相当于木桶效应
area_max = (j-i)*min(heught[i],heught[j])
求解最多的水 相当于在求解最大的面积 
首先采用暴力的方法进行遍历 这样子计算量比较大  在 时间复杂度上不能满足要求

'''
# class Solution:
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         length = len(height)
#         area_max = 0
#         for i in range(length):
#             for j in range(i,length):
#                 area = (j-i)*min(height[i],height[j])
#             if  area >= area_max:
#                 area_max = area
#         return area_max
'''

'''
class Solution:
    def maxArea(self,height):
        """
        :param height:
        :return:
        """
        max_area = 0
        left = 0
        length = len(height)
        right = length -1
        while left<right:
            max_area = max(max_area,(right - left)*min(height[left],height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area





start_time = time.time()

h = [18,17]
mysolution = Solution()
print(mysolution.maxArea(h))

end_time = time.time()
alltime = end_time - start_time

print(alltime)
