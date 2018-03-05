#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

#include "dictionary.h"

#define tsize 150000

//Define node type
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Define variable to count number of words
int count = 0;

// Variable to define if Dictionary is loaded
bool loaded

// Define hash table
node *hash_table[tsize];

//Hash function djb2 hash from http://www.cse.yorku.ca/~oz/hash.html
unsigned long hash(char *str)
{
    unsigned long hash = 5381;
    int c;

    while ((c = *str++))
    {
        hash = ((hash << 5) + hash) + c;
    }

  return hash;
}

//Loads dictionary into memory. Returns true if successful else false.

bool load(const char *dictionary)
{
    count = 0;

    // Open Dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    int l = LENGTH + 2;

    char buffer[LENGTH + 1];

    while (fgets(buffer, l, file) != NULL)
    {

        int len = strlen(buffer);
        if (buffer[len - 1] == '\n')
        buffer[--len] = '\0';

        int index = hash(buffer) % tsize;

        node *new_node = malloc(sizeof(node));

        if (new_node == NULL)
        {
            fclose(file);

            return false;
        }

        strcpy(new_node -> word, buffer);

        new_node -> next = hash_table[index];

        hash_table[index] = new_node;

        count++;
    }
    load = true;
    return true;
}

//Returns true if word is in dictionary else false.
bool check(const char *word)
{
    int len = strlen(word);
    char s[len + 1];
    s[len] = '\0';

    for (int i = 0; i < len; i++)
    s[i] = tolower(word[i]);

    int index = hash(s) % tsize;
    node *n = hash_table[index];

    while (n != NULL)
    {
        if (strcmp(s, n -> word) == 0)
        return true;
        n = n -> next;
    }

    return false;
}


// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    if (loaded)
    {
        return word_count;
    }

    else

    {
        return 0;
    }
}


//Unloads dictionary from memory. Returns true if successful else false.
//**Getting valgrind errors from check50 but not sure what to do.
bool unload(void)
{
    for (int i = 0; i < tsize; i++)
    {
        node *next = hash_table[i];

        while (next != NULL)
        {
            node *t = next;
            next = next -> next;
            free(t);
        }
    }

  count = 0;
  return true;
}