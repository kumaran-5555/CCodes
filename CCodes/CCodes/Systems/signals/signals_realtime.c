#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>
#include <my_helpers.h>


#undef DBG_ON
#define DBG_ON	1


void sighandler(int signum, siginfo_t *siginfo, void *context)
{

	printf("signum %d value %d\n", signum, siginfo->si_value);
}
	


int main()
{
	sigset_t mask, orig;
	
	struct sigaction sigact;
	union sigval sv;

	int i,j;	

	// use advanced handler
	sigact.sa_flags |= SA_SIGINFO;
	// let other signals not disturb
	sigemptyset(&sigact.sa_mask);
	sigact.sa_sigaction = sighandler;
	

	sigfillset(&mask);
	
	if(sigprocmask(SIG_BLOCK, &mask, &orig) < 0)
	{
		perror("sigprocmask()");
		exit(2);
	}
	for( i=SIGRTMIN; i<SIGRTMIN+3; i++)
	{
		if(sigaction(i, &sigact, NULL) < 0)
		{
			perror("sigaction()");
			exit(2);
		}
	}
	
	for (i=SIGRTMIN; i<SIGRTMIN+3; i++)
	{
	
		for(j=0; j<5; j++)
		{
			sv.sival_int = j;		
			
			if(sigqueue(getpid(), i,  sv) < 0)
			{
				perror("sigqueue()");
				exit(2);
			}
		}
	}

	if(sigprocmask(SIG_SETMASK, &orig, NULL) < 0)
	{
		perror("siprocmask()");
		exit(2);
	}


	


}
