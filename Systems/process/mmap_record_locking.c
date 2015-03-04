#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <my_helpers.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>





/*
 * two processes will open a same file and mmap them
 * p1 one will read the first 4 bytes(with lock), if it is 
 * odd, increment one and write it back, if it is not odd,
 * tries again
 * p2 does the same thing, but it converts even to odd
 * if the counter reaches 100, p1 and p2 exits
 */


int main(int argc, char *argv[])
{
	if (argc != 2)
	{
		printf("Usage: %s <isEvenToOddFlag>\n", argv[0]);
		exit(1);
	}
	int isEvenToOddFlag = atoi(argv[1]);
	int fd, val, sts;
		
	fd = shm_open("/newshmem", O_CREAT|O_RDWR, S_IRWXU);
	if (fd < 0)
	{
		perror("shm_open()");
		exit(1);
	}
	ftruncate(fd, sizeof(val));
		
	
	
	

	
	
	close(fd);
	shm_unlink("/newshmem");	

}
	
		
	

	
