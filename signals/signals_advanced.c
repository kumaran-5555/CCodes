#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>
#include <my_helpers.h>
#include <time.h>


#undef DBG_ON
#define DBG_ON 	1


/*
 * blocke all signal for 10 seconds
 * let other send signals
 * receive signals and print them
 */


void signal_handler(int signum, siginfo_t *info, void *opaque)
{
	printf("Recived singal %d\n", signum);
	
}

void signal_handler2(int signum)
{
	printf("Recived signum %d\n", signum);
}

int main()
{

	sigset_t set;
	sigset_t orig;
	sigemptyset(&set);
	sigaddset(&set, SIGINT);
	sigaddset(&set, SIGQUIT);
	struct sigaction sigact;
	sigact.sa_handler = signal_handler2;
	//sigact.sa_flags = SA_SIGINFO;	
	
	if(sigaction(SIGINT, &sigact, NULL) < 0)
	{
		perror("sigaction()");
		exit(2);
	}
	if(sigaction(SIGQUIT, &sigact, NULL) < 0)
	{
		perror("sigaction()");
		exit(2);
	}
	

	if(sigprocmask(SIG_BLOCK, &set, &orig) < 0)
	{
		perror("sigprocmask()");
		exit(2);
	}
	
	DBG("blocked all signals\n");
	
		
	sleep(15);

	if(sigpending(&set) < 0)
	{
		perror("sigpending()");
		exit(2);
	}

	if(sigismember(&set, SIGINT))
	{
		printf("SIGINT is pending\n");
	}
	else
	{
		printf("SIGINT is not pending\n");
	}
	
	if(sigprocmask(SIG_SETMASK, &orig, NULL)<0)
	{
		perror("sigprocmask()");
		exit(2);
	}

	DBG("unblocked all signals\n");

}
