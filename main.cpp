#include <iostream>
#include <cstring>

int main() {
    int* arr = new int[5];

    for (int i = 0; i < 5; i++) {
        arr[i] = i;
    }

    char src[] = "This string is too long";
    char dest[5];

    strcpy(dest, src);

    delete[] arr;

    return 0;
}
