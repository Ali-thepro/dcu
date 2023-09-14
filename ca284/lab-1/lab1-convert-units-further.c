/*
 convert-units-further.c
 author <Ali Ahmad>
*/


#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[]) {
    float cm = 30, inch;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 5; j++, cm++) {
            inch = cm / 2.54;
            printf("%.2f ", inch);
        }
        printf("\n");
    }


    return 0;
}
