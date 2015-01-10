#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <my_helpers.h>

#undef DBG_ON
#define DBG_ON	1





/*
 * socket()
 * sendto()/recvfrom()
 */




int main(int argc, char *argv[])
{
	int portNum, sts, socketFd;
	struct sockaddr_in sockAddr;
	char buf[1024];
	struct sockaddr_in peerSockAddr;
	int peerPortNum;
	char peerHostAddress[24];
	char *hostAddress;
	
	if( argc != 3)
	{
		printf("Usage: %s <hostAddress> <portNum>\n",argv[0]);
		exit(1);
	}
	
	hostAddress = argv[1];
	portNum = atoi(argv[2]);
	
	socketFd = socket(AF_INET, SOCK_DGRAM, 0);
	if( socketFd < 0 )
	{
		perror("socket()");
		exit(2);
	}
	DBGVAR(socketFd, "%d");
	
	sockAddr.sin_family = AF_INET;
	sockAddr.sin_port = htons(portNum);
	inet_pton(AF_INET, hostAddress, &sockAddr.sin_addr.s_addr);
	
	while((sts=read(0, buf, 1024)))
	{
		if(sts < 0)
		{
			perror("read()");
			exit(2);
		}
		buf[sts]='\0';
		sendto(socketFd, buf, sts, 0, (struct sockaddr*)&sockAddr, sizeof(sockAddr));

	}	

}	
