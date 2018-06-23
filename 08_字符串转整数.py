#coding=UTF-8
'''
题目：在找到第一个非空字符之前，需要移除掉字符串中的空格字符。如果第一个非空字符是正号或负号，选取该符号，并将其与后面尽可能多的连续的数字组合起来，这部分字符即为整数的值。如果第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

字符串可以在形成整数的字符后面包括多余的字符，这些字符可以被忽略，它们对于函数没有影响。

当字符串中的第一个非空字符序列不是个有效的整数；或字符串为空；或字符串仅包含空白字符时，则不进行转换。

若函数不能执行有效的转换，返回 0。

说明：

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。如果数值超过可表示的范围，则返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

示例 1:

输入: "42"
输出: 42
示例 2:

输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
示例 3:

输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
示例 4:

输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。
示例 5:

输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
     因此返回 INT_MIN (−231) 。

'''
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        new_str = str.strip()
        length = len(new_str)
        res = "0"
        num = 1
        if new_str =="" or new_str == "-":
        	return 0
        if new_str[0]=="-":
        	new_str = new_str[1:]
        	for i in new_str:
        		if i.isdigit() ==True:
        			res += i
        		else:
        			break
        	num = -1*int(res)
        elif new_str[0]=="+":
        	new_str = new_str[1:]
        	for i in new_str:
        		if i.isdigit() ==True:
        			res += i
        		else:
        			break
        	num = int(res)
        else:
        	for i in new_str:
        		if i.isdigit() ==True:
        			res += i
        		else:
        			break
        	num = int(res)
        if res == " ":
        	return 0
        else:
	        if num>2**31-1:
	        	return (2**31-1)
	        elif num<-2**31:
	        	return (-2**31)
	        else:
	        	return num
#//////////// 真蓝瘦!写的这么恶心的代码 把自己恶心到了。。。emm...原始人写的代码 换一个高大尚的写法
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.strip() 
        sign = 1
        if not s:
            return 0
        if s[0] in ["+", "-"]:
            if s[0] == "-":
                sign = -1
            s = s[1:]
        ans = 0
        for c in s:
            if c.isdigit():
                ans = ans * 10 + int(c)
            else:
                break
        ans *= sign
        if ans > (2**31-1):
            return (2**31-1)
        if ans < (-2**31):
            return (-2**31)
        return ans
s = "+1"
mysolution = Solution()
print(mysolution.myAtoi(s))
