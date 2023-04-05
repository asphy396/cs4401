#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

char* backuppath()
{
  char buffer[{{buffsize}}];

  printf("Input backup path please: "); fflush(stdout);

  gets(buffer);

  printf("Got path %s\n", buffer);

  return strdup(buffer);
}

int main(int argc, char **argv)
{
  backuppath();
  return 0;
}
