#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

char* backuppath()
{
  char buffer[{{buffsize}}];
  unsigned int ret;

  printf("Input backup path please: "); fflush(stdout);

  gets(buffer);

  ret = __builtin_return_address(0);

  if((ret & 0xf0000000) == 0xf0000000) {
      printf("Backup server inaccessible. (%p)\n", ret);
      _exit(1);
  }

  printf("Got path %s\n", buffer);

  return strdup(buffer);
}

int main(int argc, char **argv)
{
  backuppath();
  return 0;
}
