#include <cs50.h>
#include <stdio.h>

#define A_SIZE 4
#define B_SIZE 5
#define C_SIZE 5
#define D_SIZE 6

// TODO: Function prototype goes here
string balanced(int x[], int n);

// You should not need to edit main()
int main(void)
{

    int a[] = {17, 40, 28, 29};
    int b[] = {11, 12, 13, 14, 15};
    int c[] = {-15, -11, -13, -14, -12};
    int d[] = {0, 0, 0, 0, 0, -1};

    printf("a: %s\n", balanced(a, A_SIZE) /*? "balanced" : "not balanced"*/);
    printf("b: %s\n", balanced(b, B_SIZE) /*? "balanced" : "not balanced"*/);
    printf("c: %s\n", balanced(c, C_SIZE) /*? "balanced" : "not balanced"*/);
    printf("d: %s\n", balanced(d, D_SIZE) /*? "balanced" : "not balanced"*/);

}

// TODO: Function definition goes here
string balanced(int x[], int n)
{
    //initialize sum variables
    int suml = 0;
    int sumr = 0;

    //for even number n
    if(n % 2 == 0)
    {
        //sum left half of elements
        for (int i=0; i < (n/2); i++)
        {
            suml = suml + x[i];
        }

        //sum right half of elements
        for (int i=(n/2); i < n; i++)
        {
            sumr = sumr + x[i];
        }

        if(suml==sumr)
        {
            return "balanced";
        }

        else
        {
            return "not balanced";
        }

    }

    else
    {
        //for odd number n
        //sum left half of elements
        for (int i = 0; i < ((n/2)-0.5); i++)
        {
            suml = suml + x[i];
        }

        //sum of right half of elements
        for (int i = ((n/2) + 1.5); i < n ; i++)
        {
            sumr = sumr + x[i];
        }

        if(suml==sumr)
        {
            return "balanced";
        }

        else
        {
            return "not balanced";
        }
    }

}
