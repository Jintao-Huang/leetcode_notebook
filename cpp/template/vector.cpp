//
// Created by 29715 on 2022/4/8.
//

void prefix_sum(vector<int> &nums, vector<int> &s) {
    // 不含0
    int n = nums.size();
    s.push_back(nums[0]);
    for (int i = 1; i < n ; ++i) {
        s.push_back(s.back() + nums[i]);
    }
}