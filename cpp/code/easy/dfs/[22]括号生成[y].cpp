//
// Created by 29715 on 2022/4/8.
//

class Solution {
public:
    static void _dfs(string &path, vector<string> &ans, int left, int right, int n){
        if (left > n){
            return;
        }
        if (right > left){
            return;
        };
        if (left == n and right == n){
            ans.emplace_back(path);
        }
        path.push_back('(');
        _dfs(path, ans, left+1, right, n);
        path[left + right] = ')';
        _dfs(path, ans, left, right +1, n);
        path.pop_back();
    }


    static vector<string> generateParenthesis(int n) {
        vector<string> ans;
        string path;
        _dfs(path, ans, 0, 0, n);
        return ans;
    }
};

int main() {
    auto slt = Solution::generateParenthesis(4);
    print_container(slt);
}