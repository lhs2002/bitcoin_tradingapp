// Helper functions for music

#include <cs50.h>
#include <math.h>
#include "helpers.h"
#include <string.h>

// is_rest: Determines whether a string represents a rest
bool is_rest(string s)
{
    // TODO
    //If s not rest, return false, else return true

    if(strncmp(s, "", 1))

    {
        return false;
    }
    else
    {
        return true;
    }
}

// Duration: Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{

    if(fraction[0] == '1')
    {

        if(fraction[2] == '1')
        {
            return 8;
        }

        else if(fraction[2] == '2')
        {
            return 4;
        }

        else if(fraction[2] == '4')
        {
            return 2;
        }

        else if (fraction[2] == '8')
        {
            return 1;
        }

    }

    else if(fraction[0] == '3' && fraction[2] == '8')
    {
        return 3;
    }
    else
    {
        return 0;
    }
    return 0;
}

// Frequency: Calculates frequency (in Hz) of a note
int frequency(string note)
{
    // TODO
    // Pick 1st char and work out Freq. Use float to preserve decimals
    float f;

    switch(note[0])
    {
        case 'C':
        f = 440.0 / (pow(2.0, (9.0 / 12.0)));
        break;

        case 'D':
        f = 440.0 / (pow(2.0, (7.0 / 12.0)));
        break;

        case 'E':
        f = 440.0 / (pow(2.0, (5.0 / 12.0)));
        break;

        case 'F':
        f = 440.0 / (pow(2.0, (4.0 / 12.0)));
        break;

        case 'G':
        f = 440.0 / (pow(2.0, (2.0 / 12.0)));
        break;

        case 'A':
        f = 440.0;
        break;

        case 'B':
        f = 440.0 * (pow(2.0, (2.0 / 12.0)));
    }

    //Account for # and sharp accidentals

    if (note[1] == '#')
    {
        //sharps are 1 semitone higher. x 2^(1/12) f
        f *= pow(2.0, (1.0 / 12.0));
    }

    else if (note[1] == 'b')
    {
        //flats are 1 semitone lower. x 2^ (-1/12) f
        f /= pow(2.0, (1.0 / 12.0));
    }

//Locate last character of string. Zero indexed, hence -1 from strlen.
int Octave = note[strlen(note)-1];

switch(Octave)
    {
        case '5':
        f *= 2.0;
        break;

        case '6':
        f *= 4.0;
        break;

        case '7':
        f *= 8.0;
        break;

        case '8':
        f *= 16.0;
        break;

        case '3':
        f /= 2.0;
        break;

        case '2':
        f /= 4.0;
        break;

        case '1':
        f /= 8.0;

        case '0':
        f /= 16.0;

    }

// Round frequency value
int r = round(f);
return r;

}