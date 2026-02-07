/* Asks user to enter value for x
 * displays the resut of the following
 * polynominal: 3x^5+2x^4-5x^3-x^2+7x-6
 */
#include <stdio.h>

int main(void)
{
    int x, y, x2, x3, x4, x5;
    printf("Enter value of x:");
    scanf("%d", &x);
    x2 = x * x;
    x3 = x * x * x;
    x4 = x * x * x * x;
    x5 = x * x * x * x * x;
    y = 3 *x5 + 2 * x4 - 5 * x3 - x2 + 7 * x - 6;
    printf("3x^5+2x^4-5x^3-x^2+7x-6: %d\n", y);

    return 0;
}
