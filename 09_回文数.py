'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

'''

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        self.res = ""
        if len(str_x)<2:
            return True
        if x <0:
            return (False)
        else:
            for i in range(len(str_x)):
                self.finder(str_x,i,i+1)
                self.finder(str_x,i,i)
            #这里将获得的最长子串 和原先的 数字进行对比 如果和原来的数字相同 那么 就返回正确
            if self.res == str_x:
                return (True)
            else:
                return (False)



    def finder(self, nums, left, right):
        while left >= 0 and right < len(nums) and nums[left] == nums[right]:
            # 设置边界条件 左下标大于0 右下标 小于字符串长度 设置初始的
            # 状态设置 从同一个数字 开始向两边 拓展寻找
            left -= 1
            right += 1
        if right - left - 1 > len(self.res):
            self.res = nums[left + 1:right]
        # 不断更新 最长 回文子串
        # 保留最长子串


x = 111
mysolution = Solution()
print(mysolution.isPalindrome(x))
