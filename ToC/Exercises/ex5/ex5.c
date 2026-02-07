/* Insert dollars-and-cents 
 * add 5% tax
 */
#include <stdio.h>

int main(void)
{
    float a, b, c;
    
    printf("Enter sum: \n");
    scanf("%f", &a);
    b = 5.0f/a * 100;
    c = a + b;
    printf("Sum after tax: %.f", c);

    return 0;
}

