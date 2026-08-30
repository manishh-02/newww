#include <iostream>
#include <cstring>

int main() {
    int* arr = new int[5];

    for (int i = 0; i <= 5; i++) {
        arr[i] = i;
    }
    int* arr = new int[5];

    for (int i = 0; i <= 5; i++) {
        arr[i] = i;
    }

    std::string src = "This string is too long";
    std::string dest = src;

    delete[] arr;