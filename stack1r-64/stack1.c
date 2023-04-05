#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <err.h>

int main(int argc, char **argv)
{
  volatile int debug_password;
  char buffer[{{buffsize}}];
  char *generator_mode; 
  FILE *fp;

  generator_mode = getenv("DEBUG");

  if(generator_mode == NULL) {
      errx(1, "Please set the DEBUG environment variable\n");
  }

  debug_password = 0;
  strcpy(buffer, generator_mode);
  fp  = fopen("./flag.txt", "r");

  if(debug_password == 0x0d0a0d0a) {
      printf("You have correctly entered Debug Mode\n");
      printf("Verbosity level of errors increased\n");
      fgets(buffer, 64, (FILE*)fp);
      printf("flag: %s\n", buffer );
      exit(0);
  } else {
      printf("Try again, you got 0x%08x\n", debug_password);
  }

}
