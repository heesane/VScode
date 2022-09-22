#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS
void main(){
    
    int int1,int2,int_sum;
    printf("두 개의 정수값을 입력하시오.");
    scanf("%d %d", &int1,&int2);
    int_sum = int1 + int2;
    printf("두 정수의 합은 %d입니다.",int_sum);

}