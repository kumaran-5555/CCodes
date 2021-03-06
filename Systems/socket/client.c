#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <my_helpers.h>

#undef DBG_ON
#define DBG_ON	1


/*
 * socket()
 * connect(address, port)
 * send()/recv()
 */

int main(int argc, char * argv[])
{
	int socketFd, portNum, sts, connFd;
	char buf[1024];
	char *hostAddress;
	struct sockaddr_in sockAddr;
	
	if (argc!=3)
	{
		printf("Usage: %s <hostAddress> <portNum>\n", argv[0]);
		exit(1);
	}
	
	portNum = atoi(argv[2]);
	hostAddress = argv[1];
		
	socketFd = socket(AF_INET, SOCK_STREAM, 0);
	if(socketFd<0)
	{
		perror("socket()");
		exit(1);
	}
	DBGVAR(socketFd,"%d");

	sockAddr.sin_family = AF_INET;
	sockAddr.sin_port = htons(portNum);
	inet_pton(AF_INET, hostAddress, &sockAddr.sin_addr.s_addr);
	connFd = connect(socketFd, (struct sockaddr*)&sockAddr, sizeof(sockAddr));	
	if(connFd < 0)
	{
		perror("connect()");
		exit(1);
	}
	DBGVAR(connFd, "%d");
	
	// read from stdin and send it to server
	while((sts = read(0, buf, 1024)) > 0)
	{
		buf[sts]='\0';
		send(socketFd, buf, sts, 0);
	}
	 
	close(connFd);
	return 1;
}

