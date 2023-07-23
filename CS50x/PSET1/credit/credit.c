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
    int H;
    do
    {
        H = get_int("How many cents are you owed?\n");
    }
    while (H < 0);
    return H;
}
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
