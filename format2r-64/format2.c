#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>


void unscramble() {
  int fd;
  char buffer[64];

  if((fd = open("./flag.txt", O_RDONLY)) < 0){
    perror("open failed!\n");
    exit(1);
  }

  int c = read(fd, buffer, 64);
  write(STDOUT_FILENO, buffer, c);

  exit(0);
}


void readtext()
{
  char buffer[64];

  fgets(buffer, 64, stdin);
  printf(buffer);
  puts("Text too scrambled to translate.");
  exit(1);
}

int main(int argc, char **argv)
{  
  setbuf(stdout, NULL);
  setbuf(stdin, NULL);
  setbuf(stderr, NULL);

  printf("%p\n", &unscramble);
  readtext();
}
