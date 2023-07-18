#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
        int First;
    do
    {
        First = get_int("Enter First population: ");
    }
    while (First < 9);

    // TODO: Prompt for end size
    int Second;
    do
    {
        Second = get_int("Enter Second population: ");
    }
    while (First < Second);
    // TODO: Calculate number of years until we reach threshold
    int Years=0;
    while (First < Second)
    {
        First= First + (First/3) - (First/4)
        Years++1
    }

    // TODO: Print number of years
    print ("")
}
