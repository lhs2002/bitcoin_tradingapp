#include <stdio.h>
#include <cs50.h>

int main (void)
{
    long long cc, add, x;
    int sum, doub, total;

    // Input CC number
    do
    {
        cc = get_long_long("Credit Card Number: ");
    }
    //only continue running code for non-negative numbers
    while ( cc < 0 );

// x2 every other digit from 2nd to last, sum results

    for ( x = cc / 10, doub = 0; x > 0; x /= 100 )
    {
        if ( 2 * (x % 10) > 9 )
        {
            doub += (2 * (x % 10)) / 10;
            doub += (2 * (x % 10)) % 10;
        }
        else
            doub += 2 * (x % 10);
    }

    // sum every other digit from last
    for ( add = cc, sum = 0; add > 0; add /= 100 )
        sum += add % 10;

//total of products and summation
    total = sum + doub;

    //check that credit card number is valid. Total's last digit should be 0. Continue to identify which type of credit card if valid. else Invalid.
    if ( total % 10 == 0 )
    {
        //if credit card number is between 34... and 35 or between 37... and 38...., show Amex. Same logic applies to other cards
        if ( (cc >= 340000000000000 && cc < 350000000000000) || (cc >= 370000000000000 && cc < 380000000000000) )
            printf("AMEX\n");
        else if ( cc >= 5100000000000000 && cc < 5600000000000000 )
            printf("MASTERCARD\n");
        else if ( (cc >= 4000000000000 && cc < 5000000000000) || (cc >= 4000000000000000 && cc < 5000000000000000) )
            printf("VISA\n");
        else
            printf("INVALID\n");
    }
    else
        printf("INVALID\n");

    return 0;
}