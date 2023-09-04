#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    //Searching all width and height pixels for the black ones
    for (int i = 0; i < width; i++)
    {
        for (int j = 0; j < height; j++)
        {
            // Change all black pixels to a color of your choosing
            if (image[i][j].rgbtRed == 0 && image[i][j].rgbtGreen == 0 && image[i][j].rgbtBlue == 0)
            {
                image[i][j].rgbtRed = 242;
                image[i][j].rgbtGreen = 242;
                image[i][j].rgbtBlue = 100;
            }
        }
    }
}
