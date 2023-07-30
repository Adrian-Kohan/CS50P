#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    //getting some message
    string m = get_string("Please write a message\n");

    int bi[] = {0, 0, 0, 0, 0, 0, 0, 0};
    int i;
    for (i = 0; i < strlen(m); i++)
    {
        int j = 0;
        int de = m[i];
        while ( de > 0)
        {
            bi[j] = de%2;
            de = de/2;
            j++;
        }
    }


}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
