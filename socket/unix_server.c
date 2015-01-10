#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/un.h>
#include <my_helpers.h>
#include <string.h>


#undef DBG_ON
#define	DBG_ON	1

#define UNIX_MAX_PATH 255
int main(int argc, char *argv[])
{
	int socketFd, sts, connFd;
	char *sockName;
	struct sockaddr_un sockAddr;
	int peerAddrLen;
	char buf[1024];

	if( argc!=2 )
	{
		printf("Usage: %s <sockName>\n", argv[0]);
		exit(1);
	}

	sockName = argv[1];
	
	socketFd = socket(AF_UNIX, SOCK_STREAM, 0);
	if( socketFd<0 )
	{
		perror("socket()");
		exit(2);
	}
	DBGVAR(socketFd, "%d");
	
	sockAddr.sun_family=AF_UNIX;
	snprintf(sockAddr.sun_path,  UNIX_MAX_PATH, sockName);
	
	sts=bind(socketFd, (struct sockaddr*)&sockAddr, sizeof(sockAddr));
	
	if(sts<0)
	{
		perror("bind()");
		exit(2);
	}
	
	sts = listen(socketFd, 100);
	if(sts<0)
	{
		perror("listen()");
		exit(2);
	}

	while(1)
	{
		connFd = accept(socketFd, (struct sockaddr*)&sockAddr, &peerAddrLen);
		if(connFd<0)
		{
			perror("accept()");
			exit(2);
		}
		DBGVAR(connFd, "%d");
		DBG("accepted connection from %s\n", sockAddr.sun_path);
		while(1)
		{
			sts = recv(connFd, buf, sizeof(buf), 0);
			if(sts<0)
			{
				perror("recv");
				exit(2);
			}
			if(!sts)
			{
				DBG("peer closed the connection\n");
				close(connFd);
				break;
			}
			buf[sts]='\0';
			printf("Received %s\n", buf);
		}
		
	}

	close(socketFd);
	return 0;
}
		
	
	
