//
// Created by 29715 on 2022/4/8.
//

int longest_palindrome(string &s, int mid1, int mid2) {
    // return: lo=mid1-j+1, hi=mid+j-1
    // mid1-j>-1; mid2+j<n;
    // j<mid1+1, n-mid2
    int jmax = min(mid1 + 1, int(s.size()) - mid2);
    for (int j = 0; j < jmax; j++) {
        if (s[mid1 - j] != s[mid2 + j]) {
            return j;
        }
    }
    return jmax;
}

unordered_map<string, int> & map_str2int(vector<string> &vector_s, unordered_map<string, int> &str2int) {
    // int to string transform to string to int
    int n = vector_s.size();
    for (int i = 0; i < n; ++i) {
        str2int[vector_s[i]] = i;
    }
    return str2int;
}

unordered_map<string, vector<int>> & processing(vector<string> &wordList,
                       unordered_map<string, int> &str2int,
                       unordered_map<string, vector<int>> &mapper) {
    // string processing. *通配符 mapper
    for (auto &w: wordList) {
        int n = w.size();
        for (int i = 0; i < n; ++i) {
            string w2(w);
            w2[i] = '*';
            mapper[w2].push_back(str2int[w]);
        }
    }
    return mapper;
}