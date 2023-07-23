#include <cs50.h>
#include <stdio.h>

long get_card (void)
long AMEX (long card)
long MasC (long card)
long Visa (long card)

int main(void)
{
    long Card-number = get_card ();
    long American-express = AMEX (card);
    long Master-Card = MasC (card);
    long Visa-Card = Visa (card);
}

long get_card (void)
{
    int c;
    do
    {
        c = get_long("Enter your card number?\n");
    }
    while (c < 13 || c > 16);
    return c;
}
long AMEX (long card)
{

}
long MasC (long card)
{

}
long Visa (long card)
{

}
