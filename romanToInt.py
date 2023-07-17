# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1 。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 给定一个罗马数字，将其转换成整数。

class Solution:
    def __init__():
        print("正在将 罗马数字 转为 整型数字!")
    def roman2int(romanNum) -> int:
        # 将 简单 罗马数字 与 阿拉伯整型数值对应 创建字典
        dict_num = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        # 判断参数是否合格
        if isinstance(romanNum,str):
            for i in romanNum:
                if i not in dict_num:
                    return "error 输入错误,含有非罗马字符!"
        else:
            return "error 输入类型错误, 请输入字符串!"

        # 判断值
        romanNum_list = [dict_num[i] for i in romanNum]
        for i in range(0, len(romanNum_list)-1):
            if romanNum_list[i] < romanNum_list[i + 1]:
                romanNum_list[i] = -romanNum_list[i]



        romanInt = sum(romanNum_list)
        return romanInt

romanNum = "MCMXCIV"
intNum = Solution.roman2int(romanNum)
print(intNum)
