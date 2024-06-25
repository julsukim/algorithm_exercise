#include <stdio.h>

int sum(int a, int b);

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        int result = sum(a, b);
        printf("%d\n", result);
    }
    return 0;
}

int sum(int a, int b) {
    return a + b;
}