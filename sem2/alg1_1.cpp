#include <iostream>

struct Node {
    int data;
    Node* next;
};

bool hasCycle(Node* head) {
    if (head == nullptr) {
        return false;
    }

    Node* slow = head;
    Node* fast = head;

    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast) {
            return true;
        }
    }

    return false;
}

int main() {
    Node* head = new Node{1, nullptr};
    head->next = new Node{2, nullptr};
    head->next->next = new Node{3, nullptr};
    head->next->next->next = new Node{4, nullptr};
    head->next->next->next->next = new Node{5, nullptr};

    head->next->next->next->next->next = head->next;

    if (hasCycle(head)) {
        std::cout << "There is an intersection" << std::endl;
    } else {
        std::cout << "There is no intersection" << std::endl;
    }

    return 0;
}