# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Dict


class Solution:
    """哈希表. Ot(denominator) Os(denominator)"""
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        d = {}  # type: Dict[int, int]  # 值, 索引
        sign = ""
        if numerator // denominator < 0:
            sign = '-'
        #
        numerator = abs(numerator)
        denominator = abs(denominator)
        x, numerator = divmod(numerator, denominator)
        ans = [sign, str(x)]
        if numerator > 0:
            ans.append(".")
        #
        while numerator > 0:
            if numerator in d:
                ans.insert(d[numerator], '(')
                ans.append(')')
                break
            d[numerator] = len(ans)
            x, numerator = divmod(numerator * 10, denominator)
            ans.append(str(x))

        return "".join(ans)


numerator = -1
denominator = -6
print(Solution().fractionToDecimal(numerator, denominator))
