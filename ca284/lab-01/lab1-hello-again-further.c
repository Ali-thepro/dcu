/*
Program: lab1-hello-again-further.c
Author: Ali Ahmad
Input: A full name
Output: Print out the given name
*/

/* includes */
#include <stdio.h>
#include <stdlib.h> /* a header file with a function we might need */

int main()
{
    char name[20];
    printf("Enter your name: ");
    scanf("%s", name);
    printf("Hello\n%s\n",name);
    return(0);
}