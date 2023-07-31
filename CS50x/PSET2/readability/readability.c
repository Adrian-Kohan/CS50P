#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

//string count_word(string word);
int main(void)
{
    string text = get_string ("Text: ");


    int numC = 0;
    int numW = 1;
    int numS = 0;

    for(int i =0; i < strlen(text); i++)
    {

        if(('a' <= text[i] && text[i] <= 'z') || ('A' <= text[i] && text[i] <= 'Z'))
        {
            numC++;
        }
        int w = text[i];
        if(w == 32)
        {
            numW++;
        }

        if(w == 46 || w == 33 || w == 63 )
        {
            numS++;
        }
    }

    int L = numC*100/numW;
    int S = numS*100/numW;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int rounded = round(index);

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



//string count_word(string word)


}