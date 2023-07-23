#include <cs50.h>
#include <stdio.h>

long get_card (void);
long AMEX (long card);
long MasC (long card);
long Visa (long card);

int main(void)
{
    long card = get_card ();
    long American_express = AMEX (card);
    long Master_Card = MasC (card);
    long Visa_Card = Visa (card);
}

long get_card (void)
{
    long c;
    do
    {
        c = get_long ("Enter your card number?\n");
    }
    while (c < 1);
    return c;
}

long AMEX (long card)
{
    return 0;
}

long MasC (long card)
{
    return 0;
}

long Visa (long card)
{
    if (4000000000000000 <= card <= 4999999999999999 || 40000000000000 <= card <= 49999999999999999 )
    {
        
    }
    return 0;
}
