/* Modifies the code from ex5 based on horners rule */
#include <stdio.h>

int main(void)
{
    int x, y;
    printf("Enter value of x:");
    scanf("%d", &x);
    y = ((((3 * x + 2) * x - 5) * x - 1) * x + 7) * x - 6;
    printf("3x^5+2x^4-5x^3-x^2+7x-6: %d\n", y);

    return 0;
}
