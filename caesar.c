#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    // check for 2 arguments, if not print error message and return.
    if (argc != 2)
    {
        printf("Usage: ./caesar k \n");
        return 1;
    }

    // store valid key in int variable
    int k = atoi(argv[1]);

    // prompt user for a message to encrypt
    string message = get_string("plaintext: ");
    printf("ciphertext: ");
    for (int i = 0, n = strlen(message); i < n; i++)
    {
        //shift letters by k
        if islower(message[i])
        {
            printf("%c", (((message[i] + k) - 97) % 26) + 97);
        }
        else if isupper(message[i])
        {
            printf("%c", (((message[i] + k) - 65) % 26) + 65);
        }
        else
            printf("%c", message[i]);
    }
    printf("\n");
    return 0;
}