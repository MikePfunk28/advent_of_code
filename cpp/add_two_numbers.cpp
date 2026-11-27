#include <initializer_list>
#include <iostream>
#include <memory>

struct ListNode {
    int val;
    std::unique_ptr<ListNode> next;
    explicit ListNode(int value = 0) : val(value), next(nullptr) {}
};

class Solution {
public:
    std::unique_ptr<ListNode> addTwoNumbers(
    const ListNode* l1,
    const ListNode* l2
) {
    ListNode dummy;
    ListNode* current = &dummy;
    int carry = 0;

    while (l1 != nullptr || l2 != nullptr || carry != 0) {
        int sum = carry;

        if (l1 != nullptr) {
            sum += l1->val;
            l1 = l1->next.get();
        }

        if (l2 != nullptr) {
            sum += l2->val;
            l2 = l2->next.get();
        }

        current->next = std::make_unique<ListNode>(sum % 10);
        current = current->next.get();
        carry = sum / 10;
    }

    return std::move(dummy.next);
    }
};

std::unique_ptr<ListNode> makeList(std::initializer_list<int> values) {
    ListNode dummy;
    ListNode* current = &dummy;

    for (int value : values) {
        current->next = std::make_unique<ListNode>(value);
        current = current->next.get();
    }

    return std::move(dummy.next);
}

void printList(const ListNode* node) {
    while (node != nullptr) {
        std::cout << node->val;
        node = node->next.get();
        if (node != nullptr) {
            std::cout << " -> ";
        }
    }
    std::cout << '\n';
}

int main() {
    auto l1 = makeList({2, 4, 3});
    auto l2 = makeList({5, 6, 4});

    Solution solution;
    auto result = solution.addTwoNumbers(l1.get(), l2.get());

    printList(result.get());
}