#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
  volatile int unsecured = 0;
  char buffer[{{buffsize}}];
  FILE *fp;

  gets(buffer);
  fp  = fopen("./flag.txt", "r");

  if(unsecured != 0) {
      printf("The 'unsecured' variable has been changed!\n");
      printf("Warning! Multiool is no longer in security mode\n");
      fgets(buffer, 64, (FILE*)fp);
      printf("flag: %s\n", buffer );
  } else {
      printf("Try again?\n");
  }
}
