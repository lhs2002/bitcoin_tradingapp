#include <stdio.h>

int main(int argc, char* argv[])
{
    //check for command line usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }

    char* infile = argv[1];

    // open input file. Copied from copy.c example
    FILE* inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    unsigned char buffer[512];

    FILE* outptr = NULL;

    //jpg name to have 7 char
    char image[7];

    int n = 0;

    // search until jpg is found
    while(fread(buffer, 512, 1, inptr) == 1)
    {
        // find the beginning of an jpg. Copied from walkthrough
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3]  & 0xf0) == 0xe0)
        {

            // make name for nth image
            sprintf(image, "%03i.jpg", n);

            // open nth image file. Copied from copy.c example
            outptr = fopen(image, "w");
            if (outptr == NULL)
            {
                fclose(inptr);
                fprintf(stderr, "Could not create %s.\n", image);
                return 3;
            }

            // increment number of files
            n++;
        }

        if (outptr != NULL)
        {
            // write to image file
            fwrite(buffer, 512, 1, outptr);
        }
    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    //success
    return 0;
}