/*
 Author: Ali Ahmad
*/

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[])
{
    // check if an argument is given
    if (argc == 1) {
        printf("No input given!\n");
        return 1;
    }
    int length;
    length = atoi(argv[1]);           // initialise length and convert to an integer
    // print first row of stars
    for (int i = 0; i < length; ++i) {
        printf("*");
    }
    printf("\n");
    // print the sides excluding first and last row of stars
    for (int i = 0; i < length - 2; ++i) {
        printf("*");
        for (int j = 0; j < length - 2; ++j) {
            printf(" ");
        }
        printf("*\n");
    }
    // print last row
    for (int i = 0; i < length; ++i) {
        printf("*");
    }
    printf("\n");
    return 0;

}