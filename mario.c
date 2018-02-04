#include <stdio.h>
#include <cs50.h>

int main(void)
{
   int height;

    // ask for height, if invalid height repeat prompt
    do
    {

        height = get_int("Height: ");

    }
    while (height < 0 || height > 23);

    // for loops to print number of hashes and spaces for left and right pyramid with 2 gap in between
    for (int x = 0; x < height; x++)
    {
        for (int s = height - x; s > 1; s--)
        {
            printf(" ");
        }
        for (int h = 0; h < x + 1; h++)
        {
            printf("#");
        }
        printf("  ");
        for (int h = 0; h < x + 1; h++)
        {
            printf("#");
        }
        printf("\n");
    }
}