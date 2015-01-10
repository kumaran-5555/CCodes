#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <my_helpers.h>

#undef DBG_ON
#define DBG_ON	1


/*
 * socket()
 * bind()
 * recvfrom()/sendto()
 */


int main(int argc, char *argv[])
{

	int socketFd, sts;
	char buf[1024];
	struct sockaddr_in sockAddr;
	char *hostAddress;
	int portNum;
	char peerHostAddress[24];
	int peerPortNum;
	socklen_t peerAddrLen;

	if( argc != 3)
	{
		printf("Usage: %s <hostAddress> <portNum>\n", argv[0]);
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
	DBGVAR(socketFd,"%d");
	
	sockAddr.sin_family = AF_INET;
	sockAddr.sin_port = htons(portNum);
	inet_pton(AF_INET, hostAddress, &sockAddr.sin_addr.s_addr);
	
	sts = bind(socketFd,(struct sockaddr*)&sockAddr, sizeof(sockAddr));
	if(sts < 0)
	{
		perror("bind()");
		exit(2);
	}
	while(1)
	{
		sts = recvfrom(socketFd, buf, 1024, 0, (struct sockaddr*)&sockAddr, &peerAddrLen);
		if(sts < 0)
		{
			perror("recv()");
			exit(2);
		}
		if(sts == 0)
		{
			DBG("peer closed connection\n");
			exit(0);
		}
		buf[sts]='\0';
		peerPortNum = ntohs(sockAddr.sin_port);
		inet_ntop(AF_INET, &sockAddr.sin_addr.s_addr, peerHostAddress, sizeof(peerHostAddress));
		printf("Received from %s:%d: %s\n", peerHostAddress, peerPortNum, buf);
	}
	return 0;
}

	
