/*
 Author: Ali Ahmad
*/

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[])
{
    //initialise array with length argc - 1
    int length = argc - 1;
    int array[length];
    int count = 0;

    // loop through command line arguments and fill the array
    for (int i = 0; i < length; ++i){
        array[i] = atoi(argv[i + 1]);
    }
    // loop through the arry anf check if a number is odd, if so, increment counter
    for (int i = 0; i < length; ++i) {
        if (array[i] % 2 == 1) {
            count++;
        }
    }
    // print the count of odd numbers
    printf("%d\n", count);
    return 0;
}