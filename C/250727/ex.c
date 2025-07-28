#include <stdio.h>

int main(void)
{
    int a = 10;
    int *p = &a;
    printf("a의 값: %d\n", a);
    printf("p의 값: %d\n", p);
    printf("p의 값: %d\n", *p);
    return 0;
}