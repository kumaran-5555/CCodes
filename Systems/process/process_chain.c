#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <my_helpers.h>

#undef DBG_ON
#define DBG_ON 	0



int setupProducer(char *exe, char *argv[], int outFd)
{
	int sts;
	DBG("in producer setup\n");
	if((sts = close(STDOUT_FILENO)) < 0)
	{
		perror("close()");
		exit(2);
	}
	if((sts = dup2(outFd,STDOUT_FILENO)) < 0)
	{
		perror("dup2()");
		exit(2);
	}
	if((sts = execvp(exe, argv)) < 0)
	{
		perror("execvp()");
		exit(2);
	}
	DBG("screwed in producer setup\n");
	
}

int setupConsumer(char *exe, char *argv[], int inFd)
{
	int sts;
	DBG("in consumer setup\n");
	if((sts = close(STDIN_FILENO)) < 0)
	{
		perror("close()");
		exit(2);
	}
	
	if((sts = dup2(inFd, STDIN_FILENO)) < 0)
	{
		perror("dup2()");
		exit(2);
	}
	
	if((sts = execvp(exe, argv)) < 0)
	{
		perror("execvp()");
		exit(2);
	}
	DBG("screwed in producer setup\n");
}
	

int main()
{
	
	int pipeFd[2];
	int sts;
	char *producerExe = "/usr/bin/ls";
	char *producerArgv[] = {"/usr/bin/ls", NULL};
	char *consumerArgv[] = {"/usr/bin/cat", NULL};
	char *consumerExe = "/usr/bin/cat";
	sts = pipe(pipeFd);
	if(sts < 0)
	{
		perror("pipe()");
		exit(2);
	}
	
	sts = fork();
	if(sts < 0)
	{
		perror("fork()");
		exit(2);
	}
	if(!sts)
	{
		DBG("producer pid %d\n", getpid());
		// producer
		close(pipeFd[0]);
		setupProducer(producerExe, producerArgv, pipeFd[1]);
		// hopefull the child doesn't return
		exit(100);
	}
	DBG("Parent after creating producer\n");	
	sts = fork();
	if(sts < 0)
	{
		perror("fork()");
		exit(2);
	}
	if(!sts)
	{
		DBG("consumer pid %d\n", getpid());
		// consumer
		close(pipeFd[1]);
		setupConsumer(consumerExe, consumerArgv, pipeFd[0]);
		// should not come here
		exit(100);
	}	
	DBG("Parent after creating consumer\n");
	
	wait();
}

