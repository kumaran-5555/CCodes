#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <signal.h>


void sigsegvHandler(int signum)
{
	printf("caught SIGSEGV\n");
	return;
}


int main()
{
	int b;
	if(signal(SIGSEGV, sigsegvHandler)==SIG_ERR)
	{
		perror("signal()");
		exit(2);
	}
	int *p=(int *)0x1913139;
	b=(*p)++;
}

