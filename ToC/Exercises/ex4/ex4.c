/* A program that computes the volume
 * of a sphere with a 10 meter radius
 */
#include <stdio.h>

int main (void)
{
    float pi = 3.14159f, ra = 10 , ra3 , vol;

    ra3 = ra * ra * ra;
    vol = 4.0f/3.0f * pi * ra3;
    printf("Volume of a sphere with a 10 meter radius(4/3πr^3): %.2f\n", vol);
    
    return 0;
}    
