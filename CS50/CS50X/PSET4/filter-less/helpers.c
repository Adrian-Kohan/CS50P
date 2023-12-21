#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int Redone;
    int Greenone;
    int Blueone;
    float gray;
    for (int i = 0; i < width; i++)
    {
        for (int j = 0; j < height; j++)
        {
            // defining each variable
            Redone = image[i][j].rgbtRed;
            Greenone = image[i][j].rgbtGreen;
            Blueone = image[i][j].rgbtBlue;

            //calculating the gray color
            gray = round((Redone + Greenone + Blueone) / 3.0);

            // Changing all pixels to a gray color
            image[i][j].rgbtRed = gray;
            image[i][j].rgbtGreen = gray;
            image[i][j].rgbtBlue = gray;
        }
    }
}


// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    float Redone, Greenone, Blueone;
    float sepiaRed, sepiaGreen, sepiaBlue;
    for (int i = 0; i < width; i++)
    {
        for (int j = 0; j < height; j++)
        {
            // defining each variable
            Redone = image[i][j].rgbtRed;
            Greenone = image[i][j].rgbtGreen;
            Blueone = image[i][j].rgbtBlue;
            sepiaRed = round(.393 * Redone + .769 * Greenone + .189 * Blueone);
            sepiaGreen = round(.349 * Redone + .686 * Greenone + .168 * Blueone);
            sepiaBlue = round(.272 * Redone + .534 * Greenone + .131 * Blueone);

            //checking that any pixle's RGB color don't pass the 255 limit
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            // Changing all pixels to sepia color
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }

}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //defining a new variable which holds a row pixels
    RGBTRIPLE replacer [width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            replacer[j] = image[i][j];
        }
        for (int k = 0; k < width; k++)
        {
            // Changing all pixels to Reflect color horizontally
            image[i][k].rgbtRed = replacer[width - k - 1].rgbtRed;
            image[i][k].rgbtGreen = replacer[width - k - 1].rgbtGreen;
            image[i][k].rgbtBlue = replacer[width - k - 1].rgbtBlue;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //defining a variable that holds the copy of the image
    RGBTRIPLE holder [height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            holder[i][j] = image[i][j];
        }
    }

    // defining new variabes and relating new colors to them
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int counter = 0;
            float newred = 0;
            float newgreen = 0;
            float newblue = 0;

            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    //ckecking if the pixle is not at the edge of the image, relate new blur color to it
                    if (!(i + k < 0 || i + k >= height || j + l < 0 || j + l >= width))
                    {
                        newred += holder[i + k][j + l].rgbtRed;
                        newgreen += holder[i + k][j + l].rgbtGreen;
                        newblue += holder[i + k][j + l].rgbtBlue;
                        counter++;
                    }
                    else
                    {
                        continue;
                    }
                }
            }
            //changing all pixels to blur color

            image[i][j].rgbtRed = (int) round(newred / counter);
            image[i][j].rgbtGreen = (int) round(newgreen / counter);
            image[i][j].rgbtBlue = (int) round(newblue / counter);
        }
    }
}
