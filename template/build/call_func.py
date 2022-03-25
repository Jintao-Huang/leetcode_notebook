# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Dict


def call_func(func_name_list: List[str], args_list: List[List], env: Dict) -> List:
    ans_list = []
    for i in range(len(func_name_list)):
        func_name = func_name_list[i]
        args = args_list[i]
        if i > 0:
            args.insert(0, ans_list[0])
        ans_list.append(eval(func_name, env)(*args))
        if i == 0:
            env.update(ans_list[0].__class__.__dict__)
    return ans_list
