#include <cs50.h>
#include <stdio.h>
#include <string.h>

//string count_word(string word);
int main(void)
{
    string text = get_string ("Write some text\n");
    printf("%s\n", text);
    string list[] = "%s\n",text;
    for(int i = 0; i < strlen(text); i++)
    {
        printf("%s", list[i]);
    }

}

//string count_word(string word)
{

}