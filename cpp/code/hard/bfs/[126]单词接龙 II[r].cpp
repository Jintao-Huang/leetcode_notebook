//
// Created by 29715 on 2022/4/8.
//

class Solution {
public:
    static vector<vector<string>> findLadders(
            string &beginWord, string &endWord, vector<string> &wordList
    ) {
        unordered_set<int> s1;
        unordered_set<int> s2_step;
        unordered_map<string, vector<int>> mapper;
        unordered_map<string, int> word2int;
        if (find(wordList.begin(), wordList.end(), beginWord) == wordList.end()) {
            wordList.push_back(beginWord);
        }
        map_str2int(wordList, word2int);
        processing(wordList, word2int, mapper);
        deque<int> q;
        vector<vector<int>> graph(wordList.size());  // i -> children
        int sn = beginWord.size();
        int begin_id = word2int[beginWord];
        if (not word2int.count(endWord)){
            return {};
        }
        int end_id = word2int[endWord];
        q.push_back(begin_id);
        s1.insert(begin_id);
        bool found = false;
        while (not q.empty()) {
            int qn = q.size();
            for (int i = 0; i < qn; ++i) {
                int w_id = q.front();
                if (w_id == end_id) {
                    found = true;
                }
                string word = wordList[w_id];
                q.pop_front();


                for (int j = 0; j < sn; ++j) {
                    char c = word[j];
                    word[j] = '*';
                    for (auto &w2_id:mapper[word]) {
                        if (not s1.count(w2_id)) {
                            graph[w_id].push_back(w2_id);
                            if (not s2_step.count(w2_id)){
                                s2_step.insert(w2_id);
                                q.push_back(w2_id);
                            }
                        }
                    }
                    word[j] = c;
                }
            }
            if (found)
                break;
            s1.insert(s2_step.begin(), s2_step.end());
        }
        if(found){
            print_matrix(graph);
            vector<vector<string>> ans;
            vector<int> path{begin_id};
            dfs(path, graph, begin_id, end_id, wordList, ans);
            return ans;
        } else{
            return {};
        }

    }
};

int main() {

    string beginWord = "red", endWord = "tax";
    vector<string> wordList{"ted","tex","red","tax","tad","den","rex","pee"};
    auto ans = Solution::findLadders(beginWord, endWord, wordList);
    print_matrix(ans);
}