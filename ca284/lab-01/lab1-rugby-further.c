/*
 rugby-further.c
 author <Ali Ahmad>
*/

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[]) {
    int try = 0, conversion = 0, penalty = 0, drop_goal = 0, total = 0, check = 1;

    if (argc-1 < 4) {
        printf("You haven't entered enough values\n");
    } else {
        for (int i = 1; i < argc; i++) {

            if (atoi(argv[i]) < 0) {
                printf("You have entered a negative value\n");
                check = 0;
            }  
        }
        if (check == 1) {
            total = (atoi(argv[1]) * 5) + (atoi(argv[2]) * 2) + (atoi(argv[3]) * 3) + (atoi(argv[4]) * 3);
            printf("%d\n", total);

        }
    }

    return 0;
}