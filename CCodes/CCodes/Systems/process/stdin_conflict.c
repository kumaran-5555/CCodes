#include <stdio.h>
#include <unistd.h>
#include <my_helpers.h>
#include <stdlib.h>
#include <time.h>




/*
 * Try to read from from stdin from both parent and child and see 
 * what happens
 */



int main()
{
	char buf[1024];
	int pipefd[2];
	int sts;
	char *childArgv[] = {"/usr/bin/more", NULL};

	if(pipe(pipefd) < 0)
	{
		perror("pipe()");
		exit(2);
	}

		
	if(fork() == 0)
	{
		if(dup2(pipefd[0], STDIN_FILENO) < 0)
		{
			perror("dup()");
			exit(2);
		}
		close(pipefd[1]);
		execvp("/usr/bin/more", childArgv);

		
	}
	else
	{
		close(pipefd[0]);
		// in parent 
		while((sts = read(0, buf, 1024)) > 0)
		{
			buf[sts]='\0';
			write(pipefd[1], buf, sts);
		}
		wait();
	}
}
	

