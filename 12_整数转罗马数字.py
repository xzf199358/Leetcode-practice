#coding=UTF-8
'''
题目：罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1
得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

示例 1:

输入: 3
输出: "III"
示例 2:

输入: 4
输出: "IV"
示例 3:

输入: 9
输出: "IX"
示例 4:

输入: 58
输出: "LVIII"
解释: C = 100, L = 50, XXX = 30, III = 3.
示例 5:

输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.

'''

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ''
        # 简单粗暴！从大到小依次处理，几个关键位置分别是：
        # 1000；900；500；400；100；90；50；40；10；9；5；4；1
        # {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9;'V':5,'IV':4,'I':1}
        # 如下的的算法 没有可扩展性 根据每个节点依次往下减 最后将形成的字符串进行相加成字符串
        while num > 0:
            if num >= 1000:
                result += 'M'
                num -= 1000
            elif num >= 900:
                result += 'CM'
                num -= 900
            elif num >= 500:
                result += 'D'
                num -= 500
            elif num >= 400:
                result += 'CD'
                num -= 400
            elif num >= 100:
                result += 'C'
                num -= 100
            elif num >= 90:
                result += 'XC'
                num -= 90
            elif num >= 50:
                result += 'L'
                num -= 50
            elif num >= 40:
                result += 'XL'
                num -= 40
            elif num >= 10:
                result += 'X'
                num -= 10
            elif num >= 9:
                result += 'IX'
                num -= 9
            elif num >= 5:
                result += 'V'
                num -= 5
            elif num >= 4:
                result += 'IV'
                num -= 4
            elif num >= 1:
                result += 'I'
                num -= 1
        return result

########################## 方案2  ###########################

class Solution2:
    def intToRoman(self, num):
        """
        :param num:
        :return:
        """
        values = {'M':1000,'D':500,'C':100,'L':50, 'X':10,'V':5,'I':1}
        # special = {'CM':900,'CD':400,'XC':90,'XL':40,'IX':9,'IV':4,}
        ans = ''
        liter = ['M','D','C','L','X','V','I']
        for idex in [0,2,4]:

            k =  num // values[liter[idex]]
            # 先除 1000 获得倍数 整数
            #这里以 1000 100 10 1 作为除数 算出 倍数

            re = (num % values[liter[idex]]) // values[liter[idex+2]]
            # 余数出除 100 的倍数

            ans += k*liter[idex]
            # 获得 关于 1000 100 10 1 的对应罗马数字的个数
            #  测试  输出 print(ans)

            if re >= 9:
                #取模数为 9 的情况下 
                ans += liter[idex+2] + liter[idex]
                # 处理特殊字符 900  CM
            elif re >= 5：
                #取模数为5 6 7 8
                ans += liter[idex+1] + (re-5)*liter[idex+2]

            elif re == 4:
                ans += liter[idex+2] + liter[idex+1]
                #特殊字符 4 取模数为4 
                else:
                ans += re*liter[idex+2]
                #取模数为 0 1 2 3 的情况下

            num %= values[liter[idex+2]]
            #取模数后 进行下次循环
        return ans


t = 89
mysolutoin = Solution2()
print(mysolutoin.intToRoman(t))
