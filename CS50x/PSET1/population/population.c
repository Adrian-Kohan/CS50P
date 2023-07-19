#include <stdio.h>
#include <cs50.h>

int main (void)

{
    //First population size
        int First;
    do
    {
        First = get_int("First population size: \n");
    }
    while (First < 9);

    //Second population size
        int Second;
    do
    {
        Second = get_int("Second population size: \n");
    }
    while (First < Second);

    //Calculation of the years that it takes for the First population to reach the Second population
    int years=0;
    while (Second<First)
    {
    First=First+(First/3)-(First/4);
    years++;
    }
    //Showing the Years
    printf ("Years:%s\n",years);
}
