#define _GNU_SOURCE
#include <sched.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>




void compute()
{
	long long i=1;
	i = i<<31;

	while(i)
		i--;


	printf("%d\n", getpid());
}





/*
 * start 10 processes at different priority
 * and see the completion order
 * main process runs at max priority to create all children
 */



int main()
{
	cpu_set_t cpu_set;
	struct sched_param param;
	int maxChild = 10;
	int childStartPirority = sched_get_priority_min(SCHED_RR);
	
	param.sched_priority = sched_get_priority_max(SCHED_RR);
	if(sched_setscheduler(0, SCHED_RR, &param) < 0)
	{
		perror("sched_setscheduler()");
		exit(2);
	}

	//printf("%d\n", param.sched_priority);
	
	// run only on first cpu
	CPU_SET(0, &cpu_set);
	if(sched_setaffinity(0, sizeof(cpu_set), &cpu_set) < 0)
	{
		perror("sched_setaffinity()");
		exit(2);
	}

	// let the parent run at max realtime priority
	
	while(maxChild)
	{
		if(!fork())
		{
			param.sched_priority = childStartPirority;
			sched_setparam(0, &param);
			compute();
			exit(0);
		}
		else
		{
			maxChild--;
			childStartPirority++;
		}
	}

	
	while(wait() > 0);		

	
}


















