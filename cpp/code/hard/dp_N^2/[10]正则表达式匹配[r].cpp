//
// Created by 29715 on 2022/4/8.
//

class Solution {
public:
    bool isMatch(string &s, string &p) {
        // dp_N^2[i][j]: 匹配到这, 是否成功. 这: s[i-1], s2[j-1];
        // dp_N^2[i][j];
        //  s[i-1]==p[j-1] or .: dp_N^2[i-1][j-1]
        //  s[i=1]!=p[j-1]:
        //      p[j-1]=='*': dp_N^2[i][j-2], dp_N^2[i-1][j]
        //          p[j-2]==s[i-1]: dp_N^2[i-1][j], dp_N^2[i][j-2]
        //          p[j-2]!=s[i-1]: dp_N^2[i][j-2]
        // S: dp_N^2[0][0]=true; dp_N^2[0][j]=false; dp_N^2[i][0]=false
        // R: dp_N^2[n][m]
        int n = s.size(), m = p.size();
        vector<vector<bool>> dp(n + 1, vector<bool>(m + 1));
        dp[0][0] = true;
        for (int j = 2; j <= m; j += 2) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 2];
            }
        }

        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                if (s[i - 1] == p[j - 1] || p[j - 1] == '.') {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    if (p[j - 1] == '*') {
                        if (p[j - 2] == s[i - 1] || p[j - 2] == '.')
                            dp[i][j] = dp[i - 1][j] or dp[i][j - 2];
                        else
                            dp[i][j] = dp[i][j - 2];
                    }
                }
            }
        }
//        print_matrix(dp_N^2);
        return dp[n][m];

    }
};

int main() {
    string s("mississippi");
    string s2("mis*is*p*.");
    auto slt = Solution().isMatch(s, s2);
    cout << slt;
    s = "aa";
    s2 ="ab*a*c*";
    slt = Solution().isMatch(s, s2);
    cout << slt;
}
