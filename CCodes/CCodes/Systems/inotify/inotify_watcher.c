#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/inotify.h>
#include <my_helpers.h>


#undef DBG_ON
#define DBG_ON	1


int main(int argc, char *argv[])
{
	int inotifyFd, sts, watchFd;
	char *dirToWatch;
	struct inotify_event *event;
	char buf[4096];
	if(argc!=2)
	{
		printf("Usage: %s <dirToWatch>\n", argv[0]);
		exit(1);
	}
	dirToWatch = argv[1];	

	inotifyFd = inotify_init();
	if(inotifyFd<0)
	{
		perror("inotify_init()");
		exit(2);
	}
	DBGVAR(inotifyFd, "%d");
	
	// watch all events
	watchFd = inotify_add_watch(inotifyFd, dirToWatch, IN_ALL_EVENTS);
	if(watchFd<0)
	{
		perror("inotify_add_watch()");
		exit(2);
	}
	
	DBGVAR(watchFd, "%d");
	while(1)
	{
		sts = read(inotifyFd, buf, sizeof(buf));
		if(sts<0)
		{
			perror("read()");
			exit(2);
		}
		event=(struct inotify_event*)buf;
		if(event->mask & IN_CREATE)
		{
			printf("file created %s\n", event->name);
		}
		else
		{
			printf("unknown event %d\n", event->mask);
		}
	}

	return 0;
}

