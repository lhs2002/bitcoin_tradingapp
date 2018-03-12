#include <cs50.h>
#include <ctype.h>
#include <locale.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <wchar.h>

typedef wchar_t emoji;

emoji get_emoji(string prompt);

// You should not need to edit main()
int main(void)
{
    //Set locale according to environment variables
    setlocale(LC_ALL, "");

    //Prompt user for code point
    emoji c = get_emoji("Code point: ");

    //Print character
    printf("%lc\n", c);

}

emoji get_emoji(string prompt)
{
    //Keep prompting if invalid code point is input
    do
    {
        prompt = get_string("Code point: ");
        printf("Usage: Insert valid code\n");
    }
    // condition to return to prompt if any of the char in code point is not valid. (ie 1st char U, 2nd +, the rest alphanum)
    while (prompt[0]!= 'U' || prompt[1]!= '+' || isalnum(prompt[2]) == 0|| isalnum(prompt[3]) == 0|| isalnum(prompt[4] == 0)|| isalnum(prompt[5] == 0)|| isalnum(prompt[6] == 0));

    //Allocate memory to copy string. Copy string is necessary to change 1st 2 characters of string
    char *t = malloc((strlen(prompt) + 1) * sizeof(char));

    if (!t)
    {
        return 1;
    }

    //copy prompt string to new string
    for (int i = 0, n = strlen(prompt); i <= n; i++)
    {
        t[i] = prompt[i];
    }

    //change 1st char to 0 & 2nd to x
    t[0] = '0';
    t[1] = 'x';


    //convert to string to int so as to return int value to calling main function.
    int a = strtol(prompt, NULL, 16);

    return a;

}

