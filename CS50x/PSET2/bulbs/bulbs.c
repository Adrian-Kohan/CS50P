#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    //getting some message
    string m = get_string("Please write a message\n");

    //greating an array and change decimal to binary
    for (int i = 0; i < strlen(m); i++)
    {
        int de = m[i];
        int bi[] = {0, 0, 0, 0, 0, 0, 0, 0};
        int j = 0;
        while (de > 0)
        {
            bi[j] = de % 2;
            de = de / 2;
            j++;
        }
        //reversing the array character and show them with bulbs
        int q;
        for (q = 7; q >= 0; q--)
        {
            print_bulb(bi[q]);
        }
        printf("\n");
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
