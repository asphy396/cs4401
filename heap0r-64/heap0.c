#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <sys/types.h>

struct script_manager {
  int valid_script;
  int (*fp)(const char *);
};

int env_scan() {
  int code;
  FILE* f;

  f = fopen("./flag.txt", "r");
  fread(&code, sizeof(int), 1, f); 
  fclose(f);

  return code;
}

int main(int argc, char **argv) {
  char *d;
  struct script_manager *f;

  d = malloc(32);
  f = malloc(sizeof(struct script_manager));
  f->fp = puts;
  f->valid_script = env_scan();

  memcpy(d, argv[1], strlen(argv[1]));

  if(f->valid_script= env_scan()) {
    f->fp(d);
  }
}
