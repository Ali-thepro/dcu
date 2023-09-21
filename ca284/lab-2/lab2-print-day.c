/*
 Author: Ali Ahmad
*/

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[])
{
    // intialise day and convert to integer
    int day = atoi(argv[1]);
    // check what day of week it is
    switch (day){
        case 1:
            printf("Sunday\n");
            break;
        case 2:
            printf("Monday\n");
            break;
        case 3:
            printf("Tuesday\n");
            break;
        case 4:
            printf("Wednesday\n");
            break;
        case 5:
            printf("Thursday\n");
            break;
        case 6:
            printf("Friday\n");
            break;
        case 7:
            printf("Saturday\n");
            break;
        default:
            printf("Invalid input!\n");
            break;
    }
    return 0;
}


/*
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[])
{
    int day = atoi(argv[1]);

    char *weekdays[7] = {
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"};
    
    int array_index = day - 1;
    printf("%s\n", weekdays[array_index]);

    return 0;
}




#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	
	if ( argc != 2 ) {
		printf("One argument required\n");
		return 0;
	}

	const char *days_of_week[] = {
		"Sunday", "Monday",
		"Tuesday", "Wednesday",
		"Thursday", "Friday",
		"Saturday"};
	
	int day = atoi(argv[1]) - 1;

	if ( day > 6 || day < 0 ) {
		printf("Argument Invalid (Must be between 1 - 7)\n");
		return 0;
	}

	printf("%s\n", days_of_week[day]);
}
*/