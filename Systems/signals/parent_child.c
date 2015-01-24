#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>


void sigchldHandler(int signum)
{
	printf("caught SIGCHLD\n");
	return;
}


int main()
{
	if(signal(SIGCHLD, sigchldHandler)==SIG_ERR)
	{
		perror("signal()");
		exit(2);
	}
	if(fork())
	{
		// pause till child dies
		pause();
		// collect childs status
		wait();
	}
	else
	{
		// child
		// do something and die
		sleep(5);
	}
	return 0;
}

