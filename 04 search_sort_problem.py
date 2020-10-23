# _*_coding:utf-8_*_
# @Time    : 2020/9/4 15:27
''' 第1题
    https://leetcode-cn.com/problems/valid-anagram/
    给两个字符串s和t，判断t是否是s重排组成的单词
    例 s = 'anagram', t = 'nagaram', return True
       s = 'rat', t = 'car', return false
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        '''way1'''
        # ss = list(s)
        # tt = list(t)
        # ss.sort()
        # tt.sort()
        # return ss == tt
        '''way2'''
        # return sorted(list(s)) == sorted((list(t)))
        '''way3'''
        dict1 = {}
        dict2 = {}
        for ch in s:
            dict1[ch] = dict1.get(ch, 0) + 1
        for ch in t:
            dict2[ch] = dict2.get(ch, 0) + 1
        return dict1 == dict2

''' 第2题
    https://leetcode-cn.com/problems/search-a-2d-matrix/
    给定一个m*n的二维列表，查找一个数是否存在。列表特征：
        1 列表每行从左到右排序完成
        2 每行第一个数比上一行最后一个数大
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        '''way1'''
        for line in matrix:
            if target in line:
                return True
        return False

''' 第3题
    https://leetcode-cn.com/problems/two-sum/
    给定一个列表和一个整数，设计算法找到两个数的下标，
    使两个数之和为给定的整数，保证肯定只有一个结果
    例如，列表[1,2,5,4]与目标整数3，1+2=3，结果为(0,1)
'''


class Solution(object):
    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     n = len(nums)
    #     for i in range(n):
    #         a = nums[i]
    #         b = target - a
    #         if b in nums:
    #             j = nums.index(b)
    #             if i != j:
    #                 return ([i,j])

    def binary_search(self, li, left, right, val):
        while left <= right:
            mid = (left + right) // 2
            if val == li[mid][0]:
                return mid
            if val < li[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            None

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_nums = [[num, i] for i, num in enumerate(nums)]
        new_nums.sort(key=lambda x: x[0])
        for i in range(len(new_nums)):
            a = new_nums[i][0]
            b = target - a
            if b >= a:
                j = self.binary_search(new_nums, i + 1, len(new_nums) - 1, b)
            else:
                j = self.binary_search(new_nums, 0, i - 1, b)
            if j:
                break
        return [new_nums[i][1], new_nums[j][1]]