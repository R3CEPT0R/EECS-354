#include "name.h"

void run() {
   int *ret;
   ret = (int *)&ret + 2;
   (*ret) = (int)shellcode;
}

int main() {
   run();
   return 0;
}

