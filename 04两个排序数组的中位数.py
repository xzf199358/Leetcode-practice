#codding=UTF-8
'''
题目: 给定两个大小为m 和n 的 有序数组nums1和nums2  请找出两个有序数组的中位数
示例：nums1 = [1,3]
    nums2 = [2]
    中位数是2
示例： nums1 = [1,2]
    nums2 = [3,4]
    中位数是2.5
'''
'''
本题目的解法 可看做就是寻找中位数 因此需要将两个有序数组进行合并 并进行重新排序
重新排序之后 在进行中位数的寻找
'''

class solution:
    def __init__(self,nums1,nums2):
        self.nums1 = nums1
        self.nums2 = nums2

    def findmediansortedArrays(self):
        a = []
        a.extend(self.nums1)
        a.extend(self.nums2)
        a = sorted(a)
        length = len(a)
        if length % 2 == 0:
            num = int(length / 2)
            return (a[num] + a[num+1])/2
        else:
            num = int(length/2)
            return a[num]


n1 = [1,2,3,4]
n2 = [5,6,7,8]
medianelement = solution(n1,n2)
print(medianelement.findmediansortedArrays())
