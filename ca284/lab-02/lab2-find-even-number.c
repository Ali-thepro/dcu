/*
 Author: Ali Ahmad
*/

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[])
{
    // initialise length and array of max length 10
    int length = argc - 1;
    int array[10];
    int check = 0;                                   // intialise check variable to check if an even number is found
    // loop through array and fill it up
    for (int i = 0; i < length; ++i) {
        array[i] = atoi(argv[i + 1]);
    }
    // loop through array and check if current element is even if so print it and its index
    for (int i = 0; i < length; ++i){
        if (array[i] % 2 == 0) {
            printf("%d - %d\n", i, array[i]);
            check = 1;                               // set check to 1 indicating an even has been found
        }
    }
    // if no even number is found 
    if (check == 0) {
        printf("Not found!\n");
    }
    return 0;
}