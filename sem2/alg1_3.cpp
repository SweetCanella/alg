#include <iostream>

struct Node {
    int data;
    Node* next;
    Node* prev;
};

void append(Node*& head, int newData) {
    Node* newNode = new Node();
    newNode->data = newData;

    if (head == nullptr) {
        head = newNode;
        head->next = head;
        head->prev = head;
    } else {
        Node* tail = head->prev;
        tail->next = newNode;
        newNode->prev = tail;
        newNode->next = head;
        head->prev = newNode;
    }
}

void remove(Node*& head, int value) {
    if (head == nullptr) {
        return;
    }

    Node* current = head;
    do {
        if (current->data == value) {
            if (current->next == current) {
                delete current;
                head = nullptr;
            } else {
                current->prev->next = current->next;
                current->next->prev = current->prev;
                if (current == head) {
                    head = current->next;
                }
                delete current;
            }
            return;
        }
        current = current->next;
    } while (current != head);
}

void printList(Node* head) {
    if (head == nullptr) {
        std::cout << "Список пуст." << std::endl;
        return;
    }

    Node* current = head;
    do {
        std::cout << current->data << " ";
        current = current->next;
    } while (current != head);
    std::cout << std::endl;
}

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

    return 0;
}