//
// Created by 29715 on 2022/4/8.
//


class Solution {
public:
    long long smallestNumber(long long num) {
        if (num == 0){
            return 0;
        }
        bool pst = num >= 0;  // 0: -
        num = abs(num);
        vector<int> n;
        int n_zero = 0;
        while (num > 0) {
            long long x = num % 10;
            if (x == 0) {
                n_zero += 1;
            } else {
                n.push_back(num % 10);
            }
            num /= 10;
        }
        long long ans = 0;
        if (pst) {
            sort(n.begin(), n.end());
            ans = n[0];
            ans *= pow(10, n_zero);
            for (int i =1; i<n.size();++i){
                ans *= 10;
                ans += n[i];
            }

        } else {
            sort(n.begin(), n.end(), [](int a, int b) { return a > b; });
            ans = 0;
            for (int i =0; i<n.size();++i) {
                ans *= 10;
                ans += n[i];
            }
            ans *= pow(10, n_zero);
            ans *= -1;
        }
        return ans;
    }
};

int main() {

}