//
// Created by 29715 on 2022/4/7.
//

class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        size_t lo = 0, hi = nums.size() - 1;
        vector<tuple<int, int>> nums2(nums.size());
        for (size_t i = 0; i < nums.size(); i++) {
            nums2[i] = make_tuple(nums[i], i);
        }
        sort(nums2.begin(), nums2.end());
        while (lo < hi) {
            int ans = get<0>(nums2[lo]) + get<0>(nums2[hi]);
            if (ans == target)
                return {get<1>(nums2[lo]), get<1>(nums2[hi])};
            else if (ans > target)
                hi--;
            else
                lo++;
        }
        return {};
    }
};


class Solution2 {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); ++i) {
            int x = nums[i];
            int tmx = target - x;
            if (m.count(tmx)) {
                return {m[tmx], i};
            } else {
                m[x] = i;
            }
        }
        return {};
    }
};

int main() {
    vector<int> nums{2, 7, 11, 5};
    int target = 9;
//    auto x = Solution().twoSum(nums, target);
    auto x = Solution2().twoSum(nums, target);
    print_container(x);
    return 0;

}