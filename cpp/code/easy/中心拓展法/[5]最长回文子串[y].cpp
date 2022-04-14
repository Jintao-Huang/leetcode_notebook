//
// Created by 29715 on 2022/4/8.
//

class Solution {
public:
    string longestPalindrome(string &s) {
        int n = s.size();
        int lo = 0, hi = -1;
        for (int i = 0; i < n; i++) {
            int j = longest_palindrome(s, i, i);
            int j2 = longest_palindrome(s, i, i + 1);
            int lo_, hi_;
            if (j2 >= j) {
                lo_ = i - j2 + 1;
                hi_ = i + 1 + j2 - 1;
            } else {
                lo_ = i - j + 1;
                hi_ = i + j - 1;
            }
            if (hi_ - lo_ > hi - lo) {
                lo = lo_;
                hi = hi_;
            }
        }
        return s.substr(lo, hi - lo + 1);
    }
};

int main() {
    string s("tattarrattat");
    auto slt = Solution().longestPalindrome(s);
    cout << slt;
}