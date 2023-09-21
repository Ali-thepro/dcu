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


/*
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc == 1) {
        printf("No input given!\n");
        return 1;
    }

    int sqr_len = atoi(argv[1]);

    for (int i = 0; i < (sqr_len); i++) {
        printf("*");
    }
    printf("\n");

    for(int i = 0; i < sqr_len - 2; ++i)
	{
		for(int j = 0; j < sqr_len; ++j)
		{
			if((j == 0) || (j == sqr_len - 1))
				printf("*");
			else
				printf(" ");
		}
		printf("\n");
	}


    for(int i = 1; i < sqr_len - 1; ++i)
	{
		for(int j = 0; j < sqr_len; ++j)
		{
			if((j == 0) || (j == sqr_len - 1))
				printf("*");
			else
				printf(" ");
		}
		printf("\n");
	}
    
    for (int i = 0; i < (sqr_len); i++) {
        printf("*");
    }
    printf("\n");
    return 0;
}
*/