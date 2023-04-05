#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void starshippath()
{
  char buffer[64];
  char flagBuffer[64];
  FILE *fp;
  unsigned int ret;

  printf("Input access path please: "); fflush(stdout);

  gets(buffer);

  ret = __builtin_return_address(0);

  if((ret & 0xff000000) == 0xff000000) {
    printf("Access denied... (%p)\n", ret);
    _exit(1);
  }

  printf("Got path %s\n", buffer);

}

int main(int argc, char **argv)
{

  starshippath();

}
