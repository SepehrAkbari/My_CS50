#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string n = get_string("What is your name? ");

    printf("Hello %s!\n", n);
}
