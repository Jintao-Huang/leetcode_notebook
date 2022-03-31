# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from template.data_structure.sorted_list import SortedList


class MyCalendar:
    def __init__(self):
        self.sl = SortedList([(-5, 0), (1e9 + 5, 1e9 + 10)])

    def book(self, start: int, end: int) -> bool:
        idx = self.sl.bisect_left((start, end))
        x1 = self.sl[idx - 1]
        x2 = self.sl[idx]
        if x1[1] <= start and end <= x2[0]:
            self.sl.add((start, end))
            return True
        return False


from template.build.call_func import call_func

print(call_func(["MyCalendar", "book", "book", "book"],
                [[], [10, 20], [15, 25], [20, 30]], globals()))
