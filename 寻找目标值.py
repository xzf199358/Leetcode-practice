'''
给定一个整数数组和一个目标值 找出数组中和为目标值的两个数
示例  给定 nums = [1,2,3,4,5] 目标值为9   返回 [3,4]
'''
'''
本例例题的解法  是暴力寻找的方法  采用 两个for循环 直接寻找
'''
class solution():
    def __init__(self,nums,target):
        '''
        :param self:
        :param nums:
        :param target:
        :return:
        '''
        self.nums=nums
        self.target = target
    def findtarget(self):
        a = len(self.nums)
        for i in range(0,a):
            for j in range(i+1,a):
                num = self.nums[i] + self.nums[j]
                if num == self.target:
                    return [i,j]


s = [6,2,3,4,5]
t = 10
mytarget = solution(s,t)
print(mytarget.findtarget())
