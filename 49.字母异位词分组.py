#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for str in strs:
            str_sort = "".join(sorted(str))
            if str_sort in result:
                result[str_sort].append(str)
            else:
                result[str_sort]=[str]
        return list(result.values()) 


# @lc code=end
