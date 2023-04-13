#include <stdio.h>
#include <unistd.h>
#include <string.h>

volatile int global = 0;

int main(void){
    char buf[64];
    memset(buf,'\x00',64);

    printf("%p\n",&global);

    read(STDIN_FILENO, buf, 64);
    printf(buf);
    
    if(global != 0) printf("\nmodified!!");
    printf("\n%d\n",global);

}
