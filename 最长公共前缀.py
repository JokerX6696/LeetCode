# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
# 示例 1：
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 示例 2：
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
# 提示：
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成


class Solution:
    __name__ = '测试函数'
    def __init__(self):
        print(self.__name__,'正在继承 Solution,请稍后')
    def longestCommonPrefix(self, strs):
        # 确定最短字符串长度
        min_len = 200
        for i in strs:
            if len(i) < min_len:
                min_len = len(i)
            else:
                continue
        if min_len == 0:
            return ""
        xb = 0
        for j in range(0,min_len):
            temp_list = []
            for k in strs:
                temp_list.append(k[j])
            if len(list(set(temp_list))) == 1:
                xb += 1
                continue
            else:
                break
        if xb == 0:
            ret = ""
        else:
            ret = strs[0][:xb]
        return ret

chars = ["a"]#["flower","flow","flight"]
methods = Solution()
ret = methods.longestCommonPrefix(chars)
print(ret)


