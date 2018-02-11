#import <stdio.h>
#import <cs50.h>
#import <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    // Return if more than 2 arguments
    if (argc != 2)
    {
        printf("Usage: ./vigenere k\n");

        return 1;
    }
    // store key value in k
        string k;
        k = argv[1];

    // check if all characters are alphabetical
    for(int i = 0, j = strlen(k); i < j; i++)
    {
        if (!isalpha(k[i]))
        {
            printf("Usage: ./vigenere k\n");

            return 1;
        }
    }

    //Prompt user for plaintext and store in variable
    string plain;
    plain = get_string("Plaintext: ");

    // Loop through characters, cipher alphabetical characters
    printf("ciphertext: ");

    for (int i = 0, j = 0, n = strlen(plain); i < n; i++)
    {
        // Get key to be applied for letter
        int key = tolower(k[j % strlen(k)]) - 'a';

        //for Upper cases
        if (isupper(plain[i]))
        {
            printf("%c", 'A' + (plain[i] - 'A' + key) % 26);

            j++;
        }
        else if (islower(plain[i]))
        {
            printf("%c", 'a' + (plain[i] - 'a' + key) % 26);

            j++;
        }
        else
        {
            // return unchanged
            printf("%c", plain[i]);
        }
    }

    printf("\n");

    return 0;
}