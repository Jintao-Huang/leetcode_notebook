
class Solution {
    // dp
public:
    static bool canJump(vector<int> &nums) {
        // dp[i]: ..nums[i]是否能跳到.
        // dp[i]: dp[0]..dp[i-1]
        // S: dp[0]=true;
        // E: dp[n-1]
        int n = nums.size();
        vector<bool> dp(n);
        dp[0] = true;
        for (int i = 1; i < n; ++i) {
            for (int j =i-1; j >= 0; --j) {
                if (j + nums[j] >= i and dp[j]){
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n - 1];
    }
};

class Solution2 {
    // dp
public:
    static bool canJump(vector<int> &nums) {
        // dp[i]: ..nums[i]是否能跳到.
        // dp[i]: dp[0]..dp[i-1]
        // S: dp[0]=true;
        // E: dp[n-1]
        int n = nums.size();
        int max_ = nums[0];
        for (int i = 1; i < n; ++i) {
            if (max_ < i)
                return false;
            max_ = max(max_, i + nums[i]);
        }
        return true;
    }
};




int main() {
    vector<int> v{3, 2, 1, 0, 4};
    auto slt = Solution::canJump(v);
    auto slt2 = Solution2::canJump(v);
    cout << slt;
    cout << slt2;
}