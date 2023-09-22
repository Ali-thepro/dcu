/*
 rugby.c
 author <Ali Ahmad>
*/

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[]) {
    int try, conversion, penalty, drop_goal, total = 0;
    try = atoi(argv[1]);
    conversion = atoi(argv[2]);
    penalty = atoi(argv[3]);
    drop_goal = atoi(argv[4]);
    total = (try * 5) + (conversion * 2) + (penalty * 3) + (drop_goal * 3);
    printf("%d\n", total);
    
    return 0;
}