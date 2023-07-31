#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void)
{
    //Getting a text from user

    string text = get_string ("Text: ");

    //Calculating the letters, words and sentences

    float numC = 0;
    float numW = 1;
    float numS = 0;

    for(int i =0; i < strlen(text); i++)
    {
        //Calculating the letters

        if(('a' <= text[i] && text[i] <= 'z') || ('A' <= text[i] && text[i] <= 'Z'))
        {
            numC++;
        }

        //Calculating the words

        int w = text[i];
        if(w == 32)
        {
            numW++;
        }

        //Calculating the sentences

        if(w == 46 || w == 33 || w == 63 )
        {
            numS++;
        }
    }

    //Calculating the grade

    float L = numC*100/numW;
    float S = numS*100/numW;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    printf("%f\n", index);

    int rounded = round(index);

    //Printing the grade

    if (rounded >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (rounded < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", rounded);
    }

}
