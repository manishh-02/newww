#include <iostream>
#include <cstring>

int main() {
    int* arr = new int[5];

    for (int i = 0; i <= 5; i++) {
        arr[i] = i;
    }

    char src[] = "This string is too long";
    char dest[5];

    // Removed unsafe strcpy

    delete[] arr;

    return 0;
}
