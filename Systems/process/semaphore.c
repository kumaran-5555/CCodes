#include <semaphore.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/fcntl.h>
#include <sys/mman.h>



int doEvenToOdd(sem_t *even, sem_t *odd, int *val)
{
	int currVal;
	while (1)
	{
		// first wait on the even, and then increment
		if(sem_wait(even) < 0)
		{
			perror("sem_wait()");
			exit(2);
		}
		printf("%d val %d\n", getpid(), *val);
		*val += 1;
		currVal = *val;
		// let the, other thread get up
		if(sem_post(odd) < 0)
		{
			perror("sem_post()");
			exit(2);
		}
		if (currVal >= 100)
			break;
	}
	
	return 0;
}

int doOddToEven(sem_t *even, sem_t *odd, int *val)
{
	int currVal;
	while (1)
	{
		// first wait on the odd, and then increment
		if(sem_wait(odd) < 0)
		{
			perror("sem_wait()");
			exit(2);
		}
		printf("%d val %d\n", getpid(), *val);
		*val += 1;
		currVal = *val;
		// let the, other thread get up
		if(sem_post(even) < 0)
		{
			perror("sem_post()");
			exit(2);
		}
		if (currVal >= 100)
			break;
	}
	
	return 0;
}

		
		

int main(int argc, char *argv[])
{
	int sts, isEvenToOdd, fd;
	sem_t *even, *odd;
	int *val;

	if(argc != 2)
	{
		printf("Usage: %s <isEventToOdd>\n", argv[0]);
		exit(1);
	}
	isEvenToOdd = atoi(argv[1]);
	
	even = sem_open("/even", O_CREAT, 0600, 1);
	if(even == SEM_FAILED)
	{
		perror("sem_open()");
		exit(2);
	}
	odd = sem_open("/odd", O_CREAT, 0600, 0);
	if(even == SEM_FAILED)
	{
		perror("sem_open()");
		exit(2);
	}
	
	fd = shm_open("/shm.value", O_CREAT|O_RDWR, 0600);
	if (fd < 0)
	{
		perror("shm_get()");
		exit(2);
	}
	ftruncate(fd, sizeof(*val));
	
	val = mmap(NULL, sizeof(*val), PROT_WRITE, MAP_SHARED, fd, 0);

	if (!val)
	{
		perror("mmap()");
		exit(2);
	}
	
	if(isEvenToOdd)
	{
		doEvenToOdd(even, odd, val);
	}
	else
	{
		doOddToEven(even, odd, val);
	}

	sem_unlink("/even");
	sem_unlink("/odd");
	shm_unlink("/shm.value");


}	
	
	
	
	
		
		
		

