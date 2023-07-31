#include <cs50.h>
#include <stdio.h>
#include <string.h>

//string count_word(string word);
int main(void)
{
    string text = get_string ("Text:\n");


    int numC = 0;
    int numW = 1;
    int numS = 0;

    for(int i =0; i < strlen(text); i++)
    {

        if(('a' <= text[i] && text[i] <= 'z') || ('A' <= text[i] && text[i] <= 'Z'))
        {
            numC++;
        }
        return numC;
        int w = text[i];
        if(w == 32)
        {
            numW++;
        }
        return numW;

        if(w == 46 || w == 33 || w == 63 )
        {
            numS++;
        }
        return numS;
    }
    float L = (numC / numW) * 100;
    float S = (numS / numW) * 100;
    printf("%f %f\n", L, S);
    float index = 0.0588 * L - 0.296 * S - 15.8;
    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %f\n", index);
    }
    printf("%i %i %i\n", numC, numW, numS);



//string count_word(string word)


}