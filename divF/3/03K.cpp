Напишите программу, которая переводит целое число (возможно, отрицательное) из восьмеричной системы счисления в десятичную.
 
#include <stdio.h>
int main(){
  int n;
  scanf("%o", &n);
  printf("%d", n);
  return 0;
}
