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




/*
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    int values[10]; //Initializes array of max length 10
    int count = 0;

    for (int i = 0; i < argc; ++i)
    {
        values[i] = atoi(argv[i + 1]); //Converts char to int and store in values array
        if (values[i] % 2 == 1)    //
        {                              // Increases count variable
            ++count;                   // if odd number found
        }                              //
    }
    printf("%d\n", count);

    return 0;
}




#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{

int nr_cmd = argc;
int total = 0;

for (int i = 0; i < nr_cmd - 1; i++) {
    
    int odd_nr = atoi(argv[i]) % 2;

    if (odd_nr != 0) {
        total++;
    }
}

printf("%i\n", total);

return 0;

}
*/