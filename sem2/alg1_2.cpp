#include <iostream>

struct Node {
    int data;
    Node* next;
};

void append(Node*& head, int newData) {
    Node* newNode = new Node();
    newNode->data = newData;
    newNode->next = nullptr;

    if (head == nullptr) {
        head = newNode;
        return;
    }

    Node* last = head;
    while (last->next != nullptr) {
        last = last->next;
    }
    last->next = newNode;
}

void printList(Node* node) {
    while (node != nullptr) {
        std::cout << node->data << " ";
        node = node->next;
    }
    std::cout << std::endl;
}

int main() {
    Node* head = nullptr;

    append(head, 1);
    append(head, 4);
    append(head, 3);
    append(head, 7);
    append(head, 2);
    append(head, 5);

    int x;
    std::cin >> x;

    Node* min = nullptr;
    Node* max = nullptr;

    Node* last = head;
    while (last != nullptr) {
        if (last->data<x) {
            append(min,last->data);
        }
        else {
            append(max,last->data);
        }
        last = last->next;
    }

    printList(min);

    printList(max);

    return 0;
}