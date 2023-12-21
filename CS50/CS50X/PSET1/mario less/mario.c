#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Getting the height of pyramid from user
    int H;
    do
    {
        H = get_int("Enter the Hieght of pyramid: \n");
    }
    while (H < 1 || H > 8);

    //Greating the pyramid with #
    for (int l = 1; l <= H; l++)
    {

        //Make it right-align
        for (int s = 1; s <= H - l; s++)


        {
            printf(" ");
        }

        for (int r = 1; r <= l; r++)
        {
            printf("#");
        }
        printf("\n");
    }
}