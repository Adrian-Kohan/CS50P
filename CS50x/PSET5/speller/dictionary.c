// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Choose number of buckets in hash table
const unsigned int N = 100000;

// Hash table
node *table[N];
int dict_size = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int hash_value = hash(word);
    node *n = table[hash_value];

    while (n != NULL)
    {
        if(strcasecmp(word, n -> word) == 0 )
        {
            return true;
        }
        n -> next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // Improve this hash function
    long sum = 0;
    for(int i; i < strlen(word); i++)
    {
        sum += tolower(word[i]);
    }
    return sum % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *dict_point = fopen(dictionary, 'r')
    if (dictionary == NULL)
    {
        printf ("Can't open the %\n", dictionary);
        return false;
    }
    char next_word[LENGTH + 1];
    while(fscanf(dict_point, "%", next_word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        srtcpy(n -> word, next_word);
        int hash_value = hash(next_word);

        n -> next = table[hash_value];
        table[hash_value] = n;
        dict_size++;
    }
    fclose(dicr_point)
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return dict_size;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
