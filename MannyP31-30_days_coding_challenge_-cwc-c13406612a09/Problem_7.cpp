#include <stdio.h>
#include <math.h>
int main() {
   int a = 8;
   float area;
   float pie = 3.14;
   printf("Program to find area of circle inscribed inside a square\n");
   printf("The side of the square is %d \n", a);
   area = ((pie/4)*a*a);
   printf("The area of circle inscribed inside a square is %f \n", area);
   return 0;
}