//
// Created by 29715 on 2022/4/8.
//

#include "stdc++.h"

using namespace std;




class Solution {
public:
//    ListNode *head_p;
//    Solution() {
//        this->head_p = nullptr;
//    }

    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        int carry = 0;
        auto head = new ListNode(0);
        ListNode *p = head;
        while (l1 != nullptr and l2 != nullptr) {
            int x = l1->val;
            int y = l2->val;
            carry += x + y;
            p->next = new ListNode(carry % 10);
            carry /= 10;
            l1 = l1->next;
            l2 = l2->next;
            p = p->next;
        }
        while (l1 != nullptr) {
            int x = l1->val;
            carry += x;
            p->next = new ListNode(carry % 10);
            carry /= 10;
            l1 = l1->next;
            p = p->next;
        }
        while (l2 != nullptr) {
            int x = l2->val;
            carry += x;
            p->next = new ListNode(carry % 10);
            carry /= 10;
            l2 = l2->next;
            p = p->next;
        }
        if (carry > 0) {
            p->next = new ListNode(carry);
        }
//        this->head_p = head;
        return head->next;
    }

//    ~Solution() {
//        ListNode *p = this->head_p;
//        while (p != nullptr) {
//            auto next = p->next;
//            delete p;
//            p = next;
//        }
//    }
};

class Solution2 {
public:

    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        int carry = 0;
        auto head = new ListNode(0);
        ListNode *p = head;
        while (l1 != nullptr || l2 != nullptr || carry) {
            int x = 0, y = 0;
            if (l1 != nullptr) {
                x = l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                y = l2->val;
                l2 = l2->next;
            }
            carry += x + y;
            p->next = new ListNode(carry % 10);
            carry /= 10;
            p = p->next;
        }
        return head->next;
    }
};

int main() {
    ListNode *l1 = build_list({9, 9, 9, 9, 9, 9, 9});
    ListNode *l2 = build_list({9, 9, 9, 9});
    auto s = new Solution();
    auto s2 = new Solution2();
    ListNode *x = s->addTwoNumbers(l1, l2);
    ListNode *x2 = s2->addTwoNumbers(l1, l2);
    print_list(x);
    print_list(x2);
}