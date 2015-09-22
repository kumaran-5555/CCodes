#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <signal.h>
#include <my_helpers.h>

#undef DBG_ON
#define DBG_ON	1


void sigquitHandler(int signum)
{
	printf("caught SIGQUIT\n");
	return;
}

void sigintHandler(int signum)
{
	printf("caught SIGINT\n");
	return;
}

void sigalrmHandler(int signum)
{
	printf("caught SIGALRM\n");
	return;
}


int main()
{
	char buf[1024];

	printf("press ctrl+D or ctrl+C\n");
	if(signal(SIGINT, sigintHandler)==SIG_ERR)
	{
		perror("signal()");
		exit(2);
	}
	if(signal(SIGQUIT, sigquitHandler)==SIG_ERR)
	{
		perror("signal()");
		exit(2);
	}
	if(signal(SIGALRM, sigalrmHandler)==SIG_ERR)
	{
		perror("signal()");
		exit(2);
	}

	while(1)
	{
		alarm(5);
		pause();
	}
	return 0;
}		
	
		
	
