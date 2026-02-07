#include <stdio.h>

int main(void)
{
    int a, b, c, d, f;

    printf("Enter a dollar amount: ");
    scanf("%d", &a);
    b = a/20;
    c = (a - b * 20)/10;
    d = ((a - b * 20) - c * 10)/5;
    f = (((a - b * 20) - c * 10) - d * 5)/1;
    
    printf("$20 bills: %d\n", b);
    printf("$10 bills: %d\n", c);
    printf("$5 bills: %d\n", d);
    printf("$1 bills: %d\n", f);

    return 0;
}
