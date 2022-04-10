

class Solution {
public:
    vector<int> sortEvenOdd(vector<int> &nums) {
        vector<int> n1;
        vector<int> n2;
        for (int i = 0; i < nums.size(); i++) {
            if (i % 2 == 1) {
                n1.push_back(nums[i]);
            } else {
                n2.push_back(nums[i]);
            }
        }
        sort(n1.begin(), n1.end(), [](int a, int b) { return a > b; });
        sort(n2.begin(), n2.end());
        for (int i = 0; i < nums.size(); i++) {
            if (i % 2 == 1) {
                nums[i] = n1[i / 2];
            } else {
                nums[i] = n2[i / 2];
            }
        }
        return nums;
    }
};

int main() {

}
