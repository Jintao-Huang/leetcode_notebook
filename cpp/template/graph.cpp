//
// Created by 29715 on 2022/4/8.
//

vector<vector<string>> &dfs(vector<int> &path, vector<vector<int>> &graph, int p, int end,
                            vector<string> &wv, vector<vector<string>> &ans) {
    if (p == end) {
        vector<string> path_s;
        for (int i:path) {
            path_s.emplace_back(wv[i]);
        }
        ans.push_back(move(path_s));
    }

    for (int c:graph[p]) {
        path.push_back(c);
        dfs(path, graph, c, end, wv, ans);
        path.pop_back();
    }
    return ans;

}