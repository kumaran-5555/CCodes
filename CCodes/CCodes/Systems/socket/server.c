#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <my_helpers.h>


#undef DBG_ON
#define DBG_ON		1


/*
 * 	socket()
 * 	bind(address, port)
 * 	listen()
 * 	accept()
 * 	send()/recv
 */

int main(int argc, char *argv[])
{
	int socketFd, sts, conn;
	unsigned short portNum;
	char * address;
	struct sockaddr_in sockAddr;
	char buf[1024];
	socklen_t sockLen = sizeof(sockAddr);

	if(argc != 3)
	{
		printf("Usage: %s <address> <portNum>\n",argv[0]);
		exit(1);
	}
	portNum = atoi(argv[2]);
	DBG("portNum %d\n", portNum);
	address = argv[1];
	DBG("address %s\n", address);
	
	socketFd = socket(AF_INET, SOCK_STREAM,0);
	if(socketFd < 0)
	{
		perror("Failed to open socket");
		exit(2);
	}
	DBG("socketFd %d\n", socketFd);	

	sockAddr.sin_family = AF_INET;
	sockAddr.sin_port = htons(portNum);
	inet_pton(AF_INET, address, &sockAddr.sin_addr.s_addr);

	DBG("filled sockaddr\n");

	sts = bind(socketFd, (struct sockaddr *)&sockAddr, sizeof(sockAddr));
	if(sts < 0)
	{
		perror("");
		exit(2);
	}
	DBG("Binded to %s:%d\n",address, portNum);
	listen(socketFd, 1000);
	
	conn = accept(socketFd, (struct sockaddr*)&sockAddr, &sockLen);
	if(conn<0)
	{
		perror("conn()");
		exit(2);
	}
	inet_ntop(AF_INET, &sockAddr.sin_addr.s_addr, buf, 1024);
	DBG("got new connection from %s:%d \n", buf, ntohs(sockAddr.sin_port));
	
	while(1)
	{
		sts = recv(conn, buf, 1024, 0);
		if(sts < 0 )
		{
			perror("");
			exit(3);
		}
		if(!sts)
		{
			printf("Peer closed connection\n");
			exit(0);
		}
		buf[sts]='\0';
		printf("Received: %s\n", buf);
	}
		

	

		
	
	close(socketFd);

	
}

