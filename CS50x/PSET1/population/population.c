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
}