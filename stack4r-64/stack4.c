#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
  char buffer[0x20];
  unsigned long ret;

  gets(buffer);

  ret =  __builtin_return_address(0);

  if((ret & 0xfffffff00000 ) != 0x7ffffff00000) {
    printf("64-bit matrix calibration failed... (%p)\n", ret);
    _exit(1);
  }
}
