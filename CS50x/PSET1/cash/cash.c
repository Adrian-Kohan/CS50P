#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}


//Defining how to get_cents works
int get_cents(void)
{
    int H;
    do
    {
        H = get_int("How many cents are you owed?\n");
    }
    while (H < 0);
    return H;
}

//Defining how to calculate_quarters calculate the number of quarters

int calculate_quarters(int cents)
{

    if (cents >= 25)
    {
        int q = cents / 25;
        return q;
    }
    else
    {
        return 0;
    }
}

//Defining how to calculate_dimes calculate the number of dimes

int calculate_dimes(int cents)
{
    int di = cents / 10;
    return di;
    if (cents % 25 >= 10)
    {
        int d = (cents % 25) / 10;
        return d;
    }
    else
    {
        return 0;
    }
}

//Defining how to calculate_nickels calculate the number of nickels

int calculate_nickels(int cents)
{
    int ni = cents / 5;
    return ni;
    if (((cents % 25) % 10) >= 5)
    {
        int n = (((cents % 25) % 10) / 5);
        return n;
    }
    else
    {
        return 0;
    }
}

int calculate_pennies(int cents)
{
    int pe = cents / 1;
    return pe;
    if ((((cents % 25) % 10) % 5) >= 1)
    {
        int p = ((((cents % 25) % 10) % 5) / 1);
        return p;
    }

    else
    {
        return 0;
    }
}
