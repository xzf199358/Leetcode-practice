'''
题目:  将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：
示例：P   A   H   N
     A P L S I I G
     Y   I   R
    之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"

'''
#coding=UTF-8
class Solution:
    def convert(self,s,numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        node_length = 2*numRows-2
        #整列节点之间的长度差值
        res = ""
        if length==0 or numRows==0 or numRows==1:
            return s
        #特殊的情况下的处理 
        for i in range(numRows):
            #这里 是按行 来遍历
            for j in range(i,length,node_length):
                #这里按 下标号遍历 标号的步长为 节点的长度 这样子整列的节点的数字就被返回  
                res += s[j]
                # 这里是返回 整列上的节点的下编下标号
                if i !=0 and i != numRows-1 and j-2*i+node_length < length:
                    res += s[j-2*i+node_length]
                    #这里返回的是 出去第一行和最后一行的 中间行部分 非整列节点部分的 下标号
        return res

s = "PAYPALISHIRING"
numRows = 4
mysolution = Solution()
print(mysolution.convert(s,numRows))
