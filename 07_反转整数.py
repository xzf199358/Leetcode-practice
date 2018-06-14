#coding=UTF-8

'''
题目：给定一个 32 位有符号整数，将整数中的数字进行反转。
示例 1:
输入: 123
输出: 321
示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21
注意:
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。
根据这个假设，如果反转后的整数溢出，则返回 0。
'''


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        '''
        判断端第一位是否为符号位
        最后一位是否为 0 

        '''
        res = ""
        str_int = str(x)
        length = len(str_int)
        if x == 0:
            return x
        elif x >=0:
            for i in range(length - 1, -1, -1):
                res += str_int[i]
                # int 强制转换 str类型的 时候 自动转换成int类型的 数值 如 012 自动转换成12
            if int(res)>2**31-1:
                return 0
            else:
                return int(res)

        else:
            res = "-"
            for i in range(length - 1, 0, -1):
                res += str_int[i]
            if int(res)<-2**31:
                return 0
            else:
                return int(res)

num = 1223456
mysolution = Solution()
print(mysolution.reverse(num))
