#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    //ckecking if the program is not executed with exactly one command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    //open the input file and allocate some memory to it
    FILE *recover = fopen(argv[1], "r");
    unsigned char *temp = malloc(512);
    char *filename = malloc(3 * sizeof(int));
    int img = 0;

    //cheching if the forensic image cannot be opened for reading
    if (temp == NULL)
    {
        return 1;
    }
    if (filename == NULL)
    {
        return 1;
    }

    //while reading 512 bytes into temp
    while (fread(temp, sizeof(unsigned char), 512, recover))
    {
        //checking if temp starts with JPEG signature create a new filename then open and write to it. at the end close it
        if (temp[0] == 0xff && temp[1] == 0xd8 && temp[2] == 0xff && (temp[3] & 0xf0) == 0xe0)
        {
            sprintf(filename, "%03i.jpg", img);
            FILE *newimage = fopen(filename, "a");
            fwrite(temp, 1, 512, newimage);
            fclose(newimage);
            img ++;
        }
        else if (img != 0)
        {
            FILE *newimage = fopen(filename, "a");
            fwrite(temp, 1, 512, newimage);
            fclose(newimage);
        }
    }
    // closing all open files and free the allocated memory
    fclose(recover);
    free(temp);
    free(filename);
}