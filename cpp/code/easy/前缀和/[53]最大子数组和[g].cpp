//
// Created by 29715 on 2022/4/8.
//

class Solution {
public:
    static int maxSubArray(vector<int> &nums) {
        int min_ = 0;
        int n = nums.size();
        int ans = -IINF;
        vector<int> s;
        s.reserve(n);
        prefix_sum(nums, s);
        print_container(s);
        for (int i = 0; i < n; i++) {
            ans = max(ans, s[i] - min_);
            min_ = min(min_, s[i]);
        }
        return ans;
    }
};

class Solution2 {
public:
    static int maxSubArray(vector<int> &nums) {
        // dp[i]. 至nums[i]的最大子数组和
        // dp[i]: dp[i-1]
        // S: dp[0] = nums[0]
        // E: dp[n-1]
        int n = nums.size();
        int dp = nums[0];
        int ans = dp;
        for (int i = 1; i < n; i++) {
            dp = max(0, dp) + nums[i];
            ans = max(ans, dp);
        }
        return ans;
    }
};

int main() {
    vector<int> nums{-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout << Solution::maxSubArray(nums);
    cout << Solution2::maxSubArray(nums);
    return 0;
}