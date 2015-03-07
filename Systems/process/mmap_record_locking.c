#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <my_helpers.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/mman.h>





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
	
	int isEvenToOddFlag;
	int fd, sts;
	int *val;
	struct flock flk;
	int currVal;
	flk.l_type = F_WRLCK;
	flk.l_whence = SEEK_SET;
	flk.l_start = 0;
	flk.l_len = sizeof(*val);
	
		
	if (argc != 2)
	{
		printf("Usage: %s <isEvenToOddFlag>\n", argv[0]);
		exit(1);
	}
	isEvenToOddFlag = atoi(argv[1]);
	fd = shm_open("/newshmem", O_CREAT|O_RDWR, S_IRWXU);
	if (fd < 0)
	{
		perror("shm_open()");
		exit(1);
	}
	ftruncate(fd, sizeof(*val));
	// map the shared memory region
	val = mmap(NULL, sizeof(*val), PROT_WRITE, MAP_SHARED, fd, 0);
	if(!val)
	{
		perror("mmap()");
		exit(0);
	}	

	while(1)
	{ 
		
		flk.l_type = F_WRLCK;
		// get write lock and if val is not even increment
		fcntl(fd, F_SETLKW, flk);
		// skkipping error handling
		if((*val)%2 == 0 && isEvenToOddFlag)
		{
			// it is even, modify it
			*val = *val + 1;
		}
		else if((*val)%2== 1 && !isEvenToOddFlag)
		{
			*val = *val + 1;
		}
		currVal = *val;	
		flk.l_type = F_UNLCK;
		// unlock
		fcntl(fd, F_SETLKW, flk);
		// see if we are done
		if (currVal >= 100)
		{
			printf("%d reached %d\n", getpid(), currVal);
			break;
		}
	}
	
	close(fd);
	shm_unlink("/newshmem");	

}
	
		
	

	
