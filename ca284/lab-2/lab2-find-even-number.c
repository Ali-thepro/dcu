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




/*
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    int values[10]; //Initializes array of max length 10
    int count = 0; //Counts evens

    for (int i = 1; i < argc; ++i)
    {
        values[i - 1] = atoi(argv[i]); //Converts from char to int and stores in values array
        if (values[i - 1] % 2 == 0)
        {
            printf("%i - %i\n", i - 1, values[i - 1]); //Prints index and value
            ++count; //Increments 'count' variable
        }
    }

    if (count == 0)                 //
    {                               // If there is no
        printf("Not found!\n");     // even numbers found 
    }                               //

    return 0;
}




#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{

int count = 0;
int nr_cmd = argc;
int total = 0;

for (int i = 1; i < nr_cmd; i++) {
    
    int even_nr = atoi(argv[i]) % 2;
    int the_nr = atoi(argv[i]);

    if (even_nr == 0) {
        printf("%i - %i\n", i - 1, the_nr);
        count++;
    }
}

if (count == 0) {
    printf("Not found!\n");
}
return 0;

}
*/