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
    for(int i = 0; i < strlen(text); i++)
    {

        if(('a' <= text[i] && text[i] <= 'z') || ('A' <= text[i] && text[i] <= 'Z'))
        {
            numC++;
        }
        if(text[i] = " ")
        {
            numW++;
        }
    }

    printf("%i\n", numC);

//string count_word(string word)


}