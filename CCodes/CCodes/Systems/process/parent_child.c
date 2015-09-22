#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <my_helpers.h>

#undef DBG_ON
#define DBG_ON	1

/*
 * simple parent child communication pipe
 * parent creates a new child
 * control childs new stdout as pipe's writeend
 * child executes a command
 * parents reads child output from pipe's read end
 */

int main()
{

	
	int pid,sts;
	int pipe_fd[2];
	char buf[512];
	if(pipe(pipe_fd)<0)
	{
		perror("pipe()");
		exit(2);
	}
	DBG("rd %d wr %d\n",pipe_fd[0],pipe_fd[1]);

	pid = fork();
	if (pid<0)
	{ 
		perror("fork()");
		exit(2);
	}
	if(!pid)
	{
		close(1);
		dup2(pipe_fd[1],1);
		char *cmd = "/usr/bin/ls";
		char *argv[] = {"ls","/usr/bin", NULL};
		// inside child
		//
		execvp(cmd, argv);
	}
	else
	{
		sts = read(pipe_fd[0], buf, 512);
		if(sts<0)
		{
			perror("read()");
			exit(2);
		}
		buf[sts] = '\0';
		printf("FromParent:\n%s\n", buf);
		// inside parent
		wait();
	}
	return 0;
}

