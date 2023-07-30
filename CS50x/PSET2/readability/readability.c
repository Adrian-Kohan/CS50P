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
    int L = (numC / numW) * 100;
    int S = (numW / numS) * 100;
    int index = 0.0588 * L - 0.296 * S - 15.8;

    printf("Grade %i\n", index);

//string count_word(string word)


}