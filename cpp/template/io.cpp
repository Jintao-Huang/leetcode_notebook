//
// Created by 29715 on 2022/4/8.
//

#ifndef _UTILS
#define _UTILS
using namespace std;

template<class T>
void print_vector(vector<T> &v) {
    cout << '[';
    auto it = v.begin();
    if (it != v.end()) {
        cout << *it;
        ++it;
    }
    for (; it != v.end(); ++it) {
        cout << ' ' << *it;
    }
    cout << ']';
}

void print_mapper(unordered_map<string, int> &mapper) {
    cout << '[';
    auto it = mapper.begin();
    if (it != mapper.end()) {
        cout << '(' << it->first << ' ' << it->second << ')';
        ++it;
    }
    for (; it != mapper.end(); ++it) {
        cout << ' ' << '(' << it->first << ' ' << it->second << ')';
    }
    cout << ']';
}

template<class T>
void print_mapper(unordered_map<string, vector<T>> &mapper) {
    cout << '[';
    auto it = mapper.begin();
    if (it != mapper.end()) {
        cout << '(' << it->first << ": ";
        print_vector(it->second);
        cout << ')';
        ++it;
    }
    for (; it != mapper.end(); ++it) {
        cout << " (" << it->first << ": ";
        print_vector(it->second);
        cout << ')';
    }
    cout << ']' << '\n';
}

template<class T>
void print_matrix(vector<vector<T>> v) {
    int n = v.size();
    for (int i = 0; i < n; i++) {
        print_vector(v[i]);
        cout << '\n';
    }
}

#endif