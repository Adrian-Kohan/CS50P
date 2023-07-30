#include <cs50.h>
#include <stdio.h>
#include <string.h>

//string count_word(string word);
int main(void)
{
    string text = get_string ("Write some text\n");
    printf("%s\n", text);

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

        if(text[i] = "!" || text[i] = "." || text[i] = "?" )
        {
            numS++;
        }
    }

    printf("%i %i %i\n", numC, numW, numS);

//string count_word(string word)


}