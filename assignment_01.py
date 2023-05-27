"""Q1.Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range( len(nums)):
            complement = target -nums[i]
            if complement in hash:
                return[i,hash[complement]]
            hash[nums[i]] = i

"""Q2.Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
- Return k."""

class Solution:
    def removeElement(self, nums: list[int], val:int):
        count = 0
        for i in range(len(nums)):
            if nums[i] != val :
                nums[count] = nums[i]
                count +=1
        return count

"""Q3.Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity."""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            return sorted(nums).index(target)

"""Q4.You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits."""

class Solution:
    def plusOne(self, digits:List[int]) ->List[int]:
        num = int("".join(map(str, digits)))
        num += 1
        return [int(x) for x in str(num)]

"""Q5.You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i, item in enumerate(nums2):
            nums1[m] = nums2[i]
            i += 1
            m += 1
        nums1.sort()


"""Q6. Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""

class Solution(object):
    def containsDuplicate(self, nums):
        hset = set()
        for idx in nums:
            if idx in hset:
                return True
            else:
                hset.add(idx)


"""Q7.Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements."""


class Solution:
    def moveZeroes(self, nums: list) -> None:
        point = 0
        for qoint in range(len(nums)):
            if nums[qoint] != 0 and nums[point] == 0:
                nums[point], nums[qoint] = nums[qoint], nums[point]

            if nums[point] != 0:
                point += 1

"""Q8.You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array."""


class Solution(object):
    def findErrorNums(self, nums):
        l, dup, mis = len(nums), 0, 0
        for num in nums:
            if nums[abs(num) - 1] < 0:
                dup = abs(num)
            else:
                nums[abs(num) - 1] *= -1

        for index in range(l):
            if nums[index] > 0:
                mis = index + 1
                break

        return [dup, mis]

#End of assignment_01
