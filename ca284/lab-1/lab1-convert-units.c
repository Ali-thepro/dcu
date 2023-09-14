/*
 convert-units.c
 author <Ali Ahmad>
*/

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[]) {
    float cm, inch;
    cm = atoi(argv[1]);
    inch = cm / 2.54;

    printf("%.2f\n", inch);
    return 0;
}
