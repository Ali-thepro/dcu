/*
 rugby-further.c
 author <Ali Ahmad>
*/

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[]) {
    int try = 0, conversion = 0, penalty = 0, drop_goal = 0, total = 0, check = 0;

    if (argc-1 < 4) {
        printf("You haven't entered enough values\n");
    } else {
        for (int i = 1; i < argc; i++) {

            if (atoi(argv[i]) < 0) {
                printf("You have entered a negative value\n");
                check = 1;
            }  
        }
        if (check = 1) {
            total = (atoi(argv[1]) * 5) + (atoi(argv[2]) * 2) + (atoi(argv[3]) * 3) + (atoi(argv[4]) * 3);
            printf("%d\n", total);

        }
    }

    return 0;
}

/*
#include <stdio.h>
#include <stdlib.h>

int get_an_int();
int main() {
    int try, conversion, penalty, drop_goal, total;

    printf("Tries: ");
    try = get_an_int();
    printf("Conversions: ");
    conversion = get_an_int();
    printf("Penalties: ");
    penalty = get_an_int();
    printf("Drop-goals: ");
    drop_goal = get_an_int();

    total = (try * 5) + (conversion * 2) + (penalty * 3) + (drop_goal * 3);
    printf("%d\n", total);
}

int get_an_int() {
    int n = 0;
    scanf("%d", &n);
    while (n < 0) {
        printf("Please enter a positive integer: ");
        scanf("%d", &n);
    }
    return n;
}
*/
