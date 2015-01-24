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
	int socketFd, sts;
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
	
	sts=connect(socketFd, (struct sockaddr*)&sockAddr, sizeof(sockAddr));
	
	if(sts<0)
	{
		perror("connect()");
		exit(2);
	}
	
	while(1)
	{
		sts=read(0, buf, sizeof(buf));
		if(sts<0)
		{
			perror("read()");
			exit(2);
		}
		if(!sts)
		{
			close(socketFd);
			return 0;
		}
		buf[sts]='\0';
		sts=send(socketFd, buf, sts, 0);
		DBGVAR(sts, "%d");
	}
	return 0;
}

			

	
	
