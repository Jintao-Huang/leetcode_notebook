//
// Created by 29715 on 2022/4/8.
//

#ifndef _LINKEDLiST
#define _LINKEDLiST

struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}

    ListNode(int x) : val(x), next(nullptr) {}

    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

void print_list(ListNode *head) {
    cout << '[';
    if (head != nullptr) {
        cout << head->val;
        head = head->next;
    }

    while (head != nullptr) {
        cout << ' ' << head->val;
        head = head->next;
    }
    cout << ']' << '\n';
}

ListNode *build_list(initializer_list<int> &&l) {
    auto *head = new ListNode(0);
    auto *p = head;
    for (int x: l) {
        p->next = new ListNode(x);
        p = p->next;
    }
    return head->next;
}

#endif