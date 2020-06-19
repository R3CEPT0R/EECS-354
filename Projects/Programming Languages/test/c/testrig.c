#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "answer.h"

void test(int num, char *res)
{
    char buffer[100];
    put_stuff_in_buffer(buffer,num);
    if (!strcasecmp(buffer,res)) {
        printf("correct\n");
    } else {
        printf("%s\n", buffer);
    }
}

int main(int argc, char *argv[])
{
    test(0,"0|0x00000000|0x00000000");
    test(-4,"-4|0xfffffffc|0xfcffffff");
    test(12345678,"12345678|0x00bc614e|0x4e61bc00");
    return 0;
}
